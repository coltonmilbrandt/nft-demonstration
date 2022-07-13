import requests, os
from  pathlib import Path
from scripts.helpful_scripts import get_breed
from brownie import AdvancedCollectible

# we could use a for loop to pin everything
# filepath = "./img/pug.png"
# filename = filepath.split("/")[-1:][0]

# OVERALL GOAL - get every breed img uploaded to pinata

def main():
    # Create an array of breeds[]
    # Create an array of breeds_list_img_path[]
    breed_list = []
    breed_list_img_path = []
    files = []
    # Grab the most recent deployed version of AdvancedCollectible solidity contract
    advanced_collectible = AdvancedCollectible[-1]
    # Get the number of collectibles
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    # Loop through them to count the number of breeds
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        # Add to the array IF breed is not there yet
        if breed not in breed_list:
            breed_list.append(breed)
            # Create image path based on breeds
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_name = image_path.split("/")[-1:][0]    
            breed_list_img_path.append(image_path)
            # print(f"Breed list: {breed_list}")
            # print(f"Breed image path list: {breed_list_img_path}")
            files.append(f"('file',('{image_name}',open('{image_path}','rb'),'application/octet-stream'))")
            pin_to_pinata(breed, image_path, image_name)
            
def pin_to_pinata(breed, image_path, image_name):
    # for i in range(len(files)):
    auth_token = os.getenv("PINATA_JWT_TOKEN")

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload={
        'pinataOptions': '{"cidVersion": 1}',
        'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'
    }
    files=[
        ('file',(image_name,open(image_path,'rb'),'application/octet-stream'))
    ]
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
