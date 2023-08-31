# Fine Tuned Stable Diffusion Model


## Project Summary
The goal of this project is to use AI to create concept weapon images for the game Destiny 2. Being able to generate a plethora of concept images within minutes can be used to inspire the artists of Destiny 2 to help accelerate and empower their creative process. The process of refining ideas and crafting hand-drawn sketches can be time-consuming, often taking hours or even days to complete. Unfortunately, the majority of these efforts end up discarded in the end.. This is a very laborious process that I hope to accelerate with AI. With these models, a Destiny 2 artist would be able to generate a plethora of images with nothing but a description (Figure 1). Not only this, but you can also generate additional images based on initial images (Figure 1). Overall, the goal of this project is NOT to replace Destiny artists, but rather empower them.

#### Figure 1
|Text Input | Image Input|
|:------:|:------:|
| Futuristic Auto Rifle with a Vibrant blue barrel and a Glowing Crystal in the middle of its body. Textured. 4K. Detailed. | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/83d56c7c-9186-4236-bd26-7901ac55e578' width=150px height=150px alt=00038-2149986109> |
| Output Images | Output Images |
| ![grid-0004](https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/984d970d-e035-490c-9c37-d58e9efa3514) | ![grid-0000 (1)](https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f2cabafa-e22e-4145-b556-8c0f39cb3fdb) |



# How was it made

## Step 1) Building the Dataset
I was unable to find a dataset of high quality destiny images, so I decided to make my own. I found this website called [destinytracker.com](https://destinytracker.com/destiny-2/db/items/weapon) that had lots of statistics and userates of all of the weapons in destiny. When you click on a weapon, a high definition image shows up, and this large collection of images is what my dataset consits of. I used my webscrapping wizardry to collect all of these images, and I then posted them to [Kaggle.com](https://www.kaggle.com/datasets/elibrignac/destiny-2-weapon-images/settings).

## Step 2) Fine Tune Stable Diffusion
Fine Tuning powerful models, such as stable diffusion, is one of the most powerful and important abilities in this new age of Massive AI models. Being able to personalize multi million dollar AI models to do what you want is something that is extremely powerful and allows small buisnesses and people (such as myself) to create things that would other wise be impossible to create due to compute and data constraints.

In order to fine-tune this model, I used a google colab T4 GPU and [DreamBooth](https://github.com/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb). Training over all of the images for 3000 epochs took around 40 minutes. This 3000

# Training Image Examples
| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/175326af-5731-472a-91ea-90b4f5dfafc2' width=100% height=100% alt=Auto_Rifle_10> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/9508d4f8-17aa-4df5-91fa-9777b4564868' width=100% height=100% alt=Linear_Fusion_Rifle_26> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/def9c5da-cbee-463f-b7dc-ec92d1f29cb1' width=100% height=100% alt=Linear_Fusion_Rifle_22> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/59acfe97-fb3f-469c-a4f4-10d7e62dbe1b' width=100% height=100% alt=Hand_Cannon_9> 
|:-------:|:-------:|:-------:|:-------: |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6739d964-7bab-4107-aaeb-715a95bb412b' width=100% height=100% alt=Rocket_Launcher_2>  | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/c23cbd9c-66c7-4841-9d13-756932c35a20' width=100% height=100% alt=Auto_Rifle_1> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/105dc4bc-c5c5-415c-9635-e8575e58a5fd' width=100% height=100% alt=Hand_Cannon_10>| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/150663d9-8e9d-4f62-800b-c13f3d8d84b7' width=100% height=100% alt=Auto_Rifle_61> |   


# Model Ouput Examples (Various Prompts)

| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f292e199-5ea1-4434-997a-3dc74965e711' width=100% height=100% alt=00009-3350176890> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/1f09bffc-74dd-4d71-970d-fc4617040b54' width=100% height=100% alt=00039-663080793> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/5258f9d0-236c-4f36-bd30-4a583a27a989' width=100% height=100% alt=00016-1287976665> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/0848e109-216b-4010-9292-6907a0377a95' width=100% height=100% alt=00085-3758210331> |
|:-------:|:-------:|:-------:|:-------: |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/59886915-15be-43f4-95b4-016e15982f3c' width=100% height=100% alt=00107-3170333889> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6ea74d99-550d-46ba-9dea-e98221ea316b' width=100% height=100% alt=00062-280761565> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f78ce04b-209d-40e8-a849-d1c8eae9cfe0' width=100% height=100% alt=00027-3390551863> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/3d4650b7-739c-4ce0-87d1-c76f751e69a8' width=100% height=100% alt=00048-2875339031> |



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







