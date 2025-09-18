# delete_product.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

 
load_dotenv()
 
url = os.getenv("supabase_url")
key = os.getenv("supabase_anon_key")
sb: Client = create_client(url, key)
 
def delete_product(product_id):
    resp = sb.table("products").delete().eq("product_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete product {pid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_product(pid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("No product deleted — check product_id.")
    else:
        print("Delete cancelled.")
 
 