# Fine Tuned Stable Diffusion Model


## Project Summary
The goal of this project is to use AI to create concept weapon images for the game Destiny 2. Being able to generate a plethora of concept images within minutes can be used to inspire the artists of Destiny 2 to help accelerate and empower their creative process. The process of refining ideas and crafting hand-drawn sketches can be time-consuming, often taking hours or even days to complete. Unfortunately, the majority of these efforts end up discarded in the end.. This is a very laborious process that I hope to accelerate with AI. With these models, a Destiny 2 artist would be able to generate a plethora of images with nothing but a description (Figure 1). Not only this, but you can also generate additional images based on initial images (Figure 1). Overall, the goal of this project is NOT to replace Destiny artists, but rather empower them.

#### Figure 1
|Text Input | Image Input|
|:------:|:------:|
| Futuristic Auto Rifle with a Vibrant blue barrel and a Glowing Crystal in the middle of its body. Textured. 4K. Detailed. | <img src="https://fdbffb24-f8d3-41e0.gradio.live/file=/content/gdrive/MyDrive/sd/stable-diffusion-webui/outputs/txt2img-images/2023-08-29/00038-2149986109.png" alt="baseImg" width="100" height="100">
 |
| Output Images | Output Images |
| ![Alt text](https://fdbffb24-f8d3-41e0.gradio.live/file=/content/gdrive/MyDrive/sd/stable-diffusion-webui/outputs/txt2img-grids/2023-08-29/grid-0004.png) | ![img2img](https://fdbffb24-f8d3-41e0.gradio.live/file=/content/gdrive/MyDrive/sd/stable-diffusion-webui/outputs/img2img-grids/2023-08-29/grid-0000.png) |

# How was it made

## Step 1) Building the Dataset
I was unable to find a dataset of high quality destiny images, so I decided to make my own. I found this website called [destinytracker.com](https://destinytracker.com/destiny-2/db/items/weapon) that had lots of statistics and userates of all of the weapons in destiny. When you click on a weapon, a high definition image shows up, and this large collection of images is what my dataset consits of. I used my webscrapping wizardry to collect all of these images, and I then posted them to [Kaggle.com](https://www.kaggle.com/datasets/elibrignac/destiny-2-weapon-images/settings).

## Step 2) Fine Tune Stable Diffusion
Fine Tuning powerful models, such as stable diffusion, is one of the most powerful and important abilities in this new age of Massive AI models. Being able to personalize multi million dollar AI models to do what you want is something that is extremely powerful and allows small buisnesses and people (such as myself) to create things that would other wise be impossible to create due to compute and data constraints.

In order to fine-tune this model, I used a google colab T4 GPU and [DreamBooth](https://github.com/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb). Training over all of the images for 3000 epochs took around 40 minutes. This 3000

# Training Image Examples
| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/8cb21f8e-df5c-4c01-92e8-ad58c4cdb81a' width=100% height=100% alt=Linear_Fusion_Rifle_3> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/9508d4f8-17aa-4df5-91fa-9777b4564868' width=100% height=100% alt=Linear_Fusion_Rifle_26> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/def9c5da-cbee-463f-b7dc-ec92d1f29cb1' width=100% height=100% alt=Linear_Fusion_Rifle_22>| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/345dda4b-2c63-434c-a8bd-e87dd84b44b5' width=100% height=100% alt=Linear_Fusion_Rifle_11>
|:-------:|:-------:|:-------:|:-------: |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/175326af-5731-472a-91ea-90b4f5dfafc2' width=100% height=100% alt=Auto_Rifle_10> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/c23cbd9c-66c7-4841-9d13-756932c35a20' width=100% height=100% alt=Auto_Rifle_1> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/fd63d4ef-e2d4-40b2-a722-c1e9149270b0' width=100% height=100% alt=Auto_Rifle_8> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/150663d9-8e9d-4f62-800b-c13f3d8d84b7' width=100% height=100% alt=Auto_Rifle_61> |   
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/99738d85-49ea-4706-88d2-c1125545b0f5' width=100% height=100% alt=Pulse_Rifle_24> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/cdc5c34e-6f26-4bfc-b1a0-63a5adf799b6' width=100% height=100% alt=Pulse_Rifle_7> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/14da7a52-1c32-427f-b36d-fff54ecb8c80' width=100% height=100% alt=Pulse_Rifle_74> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/d51ce9bb-3f83-46cd-b6f2-96c1fc2b3798' width=100% height=100% alt=Pulse_Rifle_64> |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/0e6f3353-724d-4c49-9182-464c4a39ac58' width=100% height=100% alt=Hand_Cannon_7> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/4dbd367a-feff-4ec6-8e76-9a66c078c4bb' width=100% height=100% alt=Hand_Cannon_37> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/105dc4bc-c5c5-415c-9635-e8575e58a5fd' width=100% height=100% alt=Hand_Cannon_10> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/59acfe97-fb3f-469c-a4f4-10d7e62dbe1b' width=100% height=100% alt=Hand_Cannon_9> |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6e9c900f-092a-48c3-8ee0-b9d47fa0f6ee' width=100% height=100% alt=Shotgun_1> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/0b6b8395-1610-430a-b199-93df7b0c332f' width=100% height=100% alt=Shotgun_2> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/13000f60-6458-469a-ad84-a6d5f52ee105' width=100% height=100% alt=Shotgun_5> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6739d964-7bab-4107-aaeb-715a95bb412b' width=100% height=100% alt=Rocket_Launcher_2> |



# Model Ouput Examples (Various Prompts)













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







