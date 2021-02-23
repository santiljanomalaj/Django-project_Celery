import datetime
import sys
import logging

import pandas as pd
from PIL import UnidentifiedImageError
from celery import shared_task

from abanerd.models import CSVFile, CEUCredit, Provider, CEUMediaType, CEUCreditType
from abanerd.utils import get_or_create_ceu_image_object


@shared_task(bind=True)
def upload_items(self, file_id):

    """ Getting object"""
    csv_file = CSVFile.objects.get(id=file_id)
    data = pd.read_csv(csv_file.file)

    """ DROPPING EMPTY ROWS"""
    data.dropna(how='all', inplace=True)

    """ ENSURING VALUES ARE INT/FLOAT AND SETTING TO NAN IF NOT"""
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    data['ceu_credits'] = pd.to_numeric(data['ceu_credits'], errors='coerce')

    count = 0
    for index, row in data.iterrows():

        count += 1
        title = row['title']
        logging.warning(f"[Record {count}] Processing the line '{title}'")

        ceu_credit = CEUCredit.objects.filter(title=title)

        if not ceu_credit:

            provider, _ = Provider.objects.get_or_create(
                name    = row['provider_name'].strip(),
                url     = row['provider_url'].strip()
            )

            description = row['description']
            url         = row['url']
            image_url   = row['image_url']
            published_date = datetime.datetime.now()
            event_date = datetime.datetime.now()
            price       = row['price']
            media_type  = row['ceu_media_type']
            ceu_credits = row['ceu_credits']
            ceu_type    = row['ceu_type']

            """This should be switched to just get"""
            ceu_media_queryset_result, _ = CEUMediaType.objects.get_or_create(name=media_type)
            ceu_type_queryset_result, _ = CEUCreditType.objects.get_or_create(name=ceu_type)

            if not CEUCredit.objects.filter(provider=provider, title=title).exists():
                ceu_credit = CEUCredit.objects.create(

                    title       = title,
                    description = description,
                    url         = url,
                    image_url   = image_url,
                    price       = float(price),
                    credits     = float(ceu_credits),
                    media       = ceu_media_queryset_result,
                    type        = ceu_type_queryset_result,
                    provider    = provider,
                    published_date = datetime.datetime.now(),
                    event_date = datetime.datetime.now(),
                )

                """ Having issues with this field so just not going to use it for now as most items do not include it."""
                logging.warning(f"The input published_date is {row['published_date']}")
                if str(row['published_date']) not in ['nan', '']:
                    try:
                        logging.warning(f"The input published_date is {row['published_date']}")
                        published_date = datetime.datetime.strptime(row['published_date'], '%m/%d/%Y')
                        logging.warning(f"The published_data is {published_date}")
                        ceu_credit.published_date = published_date
                    except ValueError:
                        logging.warning("chekcing error in exception",ValueError)
                        pass

                '''MAKE IMAGE FILE OR ASSIGN CURRENT ONE '''
                if str(image_url) != 'nan':

                    logging.info(f"Making an image from the image file located at: {image_url}")

                    try:
                        ceu_credit.image = get_or_create_ceu_image_object(image_url)
                    except UnidentifiedImageError:
                        """ 
                        This was added due to an image that while it was a jpg and the URL returned an image PIL
                        did not agree. Therefore, simply managing it wit this exception insead -- I am missing out on
                        some of these.
                        """
                        logging.warning(f"The url {image_url} is not a valid image")
                        pass
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        raise

                ceu_credit.save()
        else:
            logging.warning(f'The credit "{title}" is already present.')
