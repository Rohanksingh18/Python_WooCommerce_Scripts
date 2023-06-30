
# WooCommerce Product Deletion Script using Python

This script deletes products from a WooCommerce store that do not have any associated images. It utilizes the WooCommerce API to interact with the store and perform the deletion process.

## Prerequisites

- Python 3.6 or above
- `woocommerce` library (install via `pip install woocommerce`)

## Setup

1. Clone this repository or download the script file.

2. Install the required dependencies by running the following command:

   ```
   pip install woocommerce
   ```

3. Set up the necessary environment variables for the WooCommerce API credentials:

   - `WOO_URL`: The URL of your WooCommerce store.
   - `WOO_KEY`: The consumer key for the WooCommerce API.
   - `WOO_SECRET`: The consumer secret for the WooCommerce API.

   You can either set these variables directly in your environment or create a `.env` file in the script's directory and define them there.

4. Adjust the pagination parameters in the script if needed. The default `per_page` value is set to 10, but you can modify it based on your requirements.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command:

   ```
   python delete_products_without_images.py
   ```

   The script will connect to your WooCommerce store using the provided credentials and delete products that do not have any associated images.

3. Once the script finishes, it will display a summary of the deletion process, including the total number of products, deleted products, and remaining products.

## Notes

- This script assumes that you have already set up a WooCommerce store and have the necessary API credentials to connect to it.

- The script utilizes pagination to retrieve all products from the WooCommerce API, ensuring that no products are left out during the deletion process.

- It is recommended to test this script on a development or staging environment before running it on a production store. Always perform backups and exercise caution when deleting products.



## Acknowledgments

This script utilizes the [woocommerce](https://pypi.org/project/woocommerce/) library for Python, which simplifies the interaction with the WooCommerce API.

