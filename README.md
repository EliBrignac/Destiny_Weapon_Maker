# Fine Tuned Stable Diffusion Model


# Building the Dataset
I was unable to find a dataset of high quality destiny images, so I decided to make my own. I found this website called [destinytracker.com](https://destinytracker.com/destiny-2/db/items/weapon) that had lots of statistics and userates of all of the weapons in destiny. When you click on a weapon, a high definition image shows up, and this large collection of images is what my dataset consits of. I used my webscrapping wizardry to get all of these images, and I posted them to [Kaggle.com](https://www.kaggle.com/datasets/elibrignac/destiny-2-weapon-images/settings).

# Fine Tuning the model
Fine Tuning these powerful models such as stable diffusion is, in my mind, one of the most powerful and important abilities in this new age of Massive AI models. Being able to fine-tune a multi million dollar AI model to do what you want is something that is extremely powerful and impactful and can allow small buisnesses and people (such as myself) to create things that were previously impossible.

In order to fine-tune this model, I used a google colab T4 GPU and [DreamBooth](https://github.com/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb). Training over all of the images for 3000 epochs took around 40 minutes. This 3000





# Text → Image
| Image 1                  | Image 2                  |  Image 3|
|:------------------------:|:------------------------:|   :------------------------:|
| <img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/d63e42b8-2d35-4103-922f-807870a85ded" width="100%" height="100%" alt="grid-0014"> |<img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/3a8cece7-64a6-412f-b1d7-c3c3dd41644c" width="100%" height = "100%" alt="grid-0016">| <img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/a1786492-ede7-4b04-a1c3-21d99c9c7332" width=100% height = 100% alt="grid-0003" >|
| Linear Fusion Rifle with a Pikachu Theme              |Combat Bow that looks like it was made by Apple Inc. AAPL. Futuristic. Exotic. HD. 4K  | Ethereal Trace Rifle, emitting a captivating aura of enigmatic power. |

# Image → Image
#### Generated Images Description
- (I forgot to save the prompt I used for these)
  
| Generated Images | My Fav       | More like my Fav               |
|:-----------------------:|:-----------------------:|:-----------------------:|
|<img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/0f9cd19f-2e49-4432-8c9a-8029ac469e7e" alt="Image" width=100% height =100%>  |<img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/5377e939-999e-4667-bfe1-3ed00d6be03c" alt="Image" width=100% height =100%> | <img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/9fa292e2-7c32-4852-8750-dc700cb14b87" alt="Image" width=100% height =100%> |
| (I forgot to save the prompt I used for these). | This image I like alot, and I want more weapon designs like this one | The generated weapon designs similar to the prior image |



# Masking
#### Image Description
- Rocket Launcher that boasts a fierce dragon mouth at its tip, intricately sculpted with snarling teeth and fiery eyes, embodying both power and mythical allure.

| Image 1                 | Image 2                 | Image 3                 |
|:-----------------------:|:-----------------------:|:-----------------------:|
|<img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f47280cf-13ec-4beb-99e3-fa12510d61af" alt="Image" width=100% height =100%> |  <img alt="PaintingOverForEyeball" src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f24ee6b1-a3f6-427e-a4c7-51f024019433" width=100% height=100% > | <img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/12b5eafb-4857-44d1-afca-b55f5ca9cb57" alt="Image" width=100% height =100%>|
| As you can see, there is no eye | Paint over where you want the Eye | It creates an Eye! |







