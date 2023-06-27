import os
from woocommerce import API
import logging as logger

# WooCommerce API credentials.
url = os.environ.get('WOO_URL')
consumer_key = os.environ.get('WOO_KEY')
consumer_secret = os.environ.get('WOO_SECRET')

# Initialize WooCommerce API (Payload).
wcapi = API(
    url=url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    wp_api=True,
    version="wc/v3"
)

def delete_products_without_images():
    total_products = 0
    deleted_products = 0

    # Define pagination parameters (As per page default is 10).
    page = 1
    per_page = 100  # Adjust the value based on your needs.

    while True:
        # Retrieve products using pagination.
        products = wcapi.get("products", params={"page": page, "per_page": per_page}).json()

        if not products:
            break  # No more products to retrieve, exit the loop.

        total_products += len(products)

        # Iterate over each product.
        for product in products:
            product_id = product["id"]

            # Check if the product has any images.
            if not product["images"]:
                # Delete the product.
                wcapi.delete("products/{}".format(product_id), params={"force": True})
                deleted_products += 1

        page += 1  # Move to the next page.

    # Calculate remaining products.
    remaining_products = total_products - deleted_products

    # Print the summary.
    print("Summary:")
    logger.info("Printing total number of products")
    print("Total products: {}".format(total_products))
    logger.info("Printing total number of deleted products")
    print("Deleted products: {}".format(deleted_products))
    logger.info("Printing total number of remaining products")
    print("Remaining products: {}".format(remaining_products))


# Call the function to delete products without images.
delete_products_without_images()









