# Fine Tuned Stable Diffusion Model


## Project Summary
The goal of this project is to use AI to create concept weapon images for the game Destiny 2. I figured that the best way to accomplish this was to fine-tune a stable diffusion model on already existing destiny weapons. Being able to generate a plethora of concept images within minutes can be used to inspire the artists of Destiny 2 to help accelerate and empower their creative process. The old school way of refining ideas and crafting hand-drawn sketches can be time-consuming, often taking hours or even days to complete. In addition to this, the majority of these concept drawings end up discarded and only a select few make into the product, meaning countless hours of drawings, refinement, and ideas generation is waisted which is very inefficient. With my Destiny Weapon generator models, I believe that this waisted time can be reduced by orders of magnitude. With these models, a Destiny 2 artist would be able to generate a plethora of images within seconds, with nothing but a description (Figure 1). Not only this, but you can also generate additional images based on initial images (Figure 1). Overall, the goal of this project is NOT to replace Destiny artists, but rather <u>empower</u> them to accelerate their creative process and reduce the time spent in the concept generation and concept refinement stages.

#### Figure 1
|Text Input (text2img) | Image Input (img2img)|
|:------:|:------:|
| ↓ |  ↓ |
| Futuristic Auto Rifle with a Vibrant blue barrel and a Glowing Crystal in the middle of its body. Textured. 4K. Detailed. | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/83d56c7c-9186-4236-bd26-7901ac55e578' width=150px height=150px alt=00038-2149986109> |
| Output Images | Output Images |
| ↓ | ↓ |
| ![grid-0004](https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/984d970d-e035-490c-9c37-d58e9efa3514) | ![grid-0000 (1)](https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f2cabafa-e22e-4145-b556-8c0f39cb3fdb) |



# How was it made

## Step 1) Building the Dataset
I was unable to find a dataset of high quality destiny images, so I decided to make my own. I found this website called [destinytracker.com](https://destinytracker.com/destiny-2/db/items/weapon) that had lots of statistics and userates of all of the weapons in destiny. When you click on a weapon, a high definition image shows up, and this large collection of images is what my dataset consits of. I used my webscrapping wizardry to collect all of these images, and I then posted them to [Kaggle.com](https://www.kaggle.com/datasets/elibrignac/destiny-2-weapon-images/settings).

## Step 2) Fine Tune Stable Diffusion
Fine Tuning powerful models, such as stable diffusion, is one of the most powerful and important abilities in this new age of Massive AI models. Being able to personalize multi million dollar AI models to do what you want allows small buisnesses and people (such as myself) to create things that would otherwise be impossible to create.

In order to fine-tune this model, I used a google colab T4 GPU and [DreamBooth](https://github.com/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) ([Paper Here](https://arxiv.org/pdf/2208.12242.pdf). Training over all of the images for 3000 epochs took around 40 minutes. I saved the model at 1000, 2000, and 3000 epochs and all models can be found on hugging face to be locally downloaded and used. Visit the DreamBooth link for a colab notebook that can walk you through how to use the models. Interaction with the model is through [Gradio UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui), where there are <u>TONS</u> of parameters that you can play with or read more about [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui). The things that I found to be most helpful are listed at the bottom of this README in the Tips and Tricks section. I do reccommend looking into all of the functionality of the Gradio UI because it truly is very impressive.

#### Training Image Examples
| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/175326af-5731-472a-91ea-90b4f5dfafc2' width=100% height=100% alt=Auto_Rifle_10> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/9508d4f8-17aa-4df5-91fa-9777b4564868' width=100% height=100% alt=Linear_Fusion_Rifle_26> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/def9c5da-cbee-463f-b7dc-ec92d1f29cb1' width=100% height=100% alt=Linear_Fusion_Rifle_22> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/59acfe97-fb3f-469c-a4f4-10d7e62dbe1b' width=100% height=100% alt=Hand_Cannon_9> 
|:-------:|:-------:|:-------:|:-------: |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6739d964-7bab-4107-aaeb-715a95bb412b' width=100% height=100% alt=Rocket_Launcher_2>  | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/c23cbd9c-66c7-4841-9d13-756932c35a20' width=100% height=100% alt=Auto_Rifle_1> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/105dc4bc-c5c5-415c-9635-e8575e58a5fd' width=100% height=100% alt=Hand_Cannon_10>| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/150663d9-8e9d-4f62-800b-c13f3d8d84b7' width=100% height=100% alt=Auto_Rifle_61> |   


#### Model Ouput Examples (Various Prompts)

| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f292e199-5ea1-4434-997a-3dc74965e711' width=100% height=100% alt=00009-3350176890> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/1f09bffc-74dd-4d71-970d-fc4617040b54' width=100% height=100% alt=00039-663080793> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/5258f9d0-236c-4f36-bd30-4a583a27a989' width=100% height=100% alt=00016-1287976665> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/0848e109-216b-4010-9292-6907a0377a95' width=100% height=100% alt=00085-3758210331> |
|:-------:|:-------:|:-------:|:-------: |
 | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/59886915-15be-43f4-95b4-016e15982f3c' width=100% height=100% alt=00107-3170333889> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/6ea74d99-550d-46ba-9dea-e98221ea316b' width=100% height=100% alt=00062-280761565> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f78ce04b-209d-40e8-a849-d1c8eae9cfe0' width=100% height=100% alt=00027-3390551863> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/3d4650b7-739c-4ce0-87d1-c76f751e69a8' width=100% height=100% alt=00048-2875339031> |


# Main Features and Functions

## Masking
#### Image Description
- Rocket Launcher that boasts a fierce dragon mouth at its tip, intricately sculpted with snarling teeth and fiery eyes, embodying both power and mythical allure.

| Image 1                 | Image 2                 | Image 3                 |
|:-----------------------:|:-----------------------:|:-----------------------:|
|<img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f47280cf-13ec-4beb-99e3-fa12510d61af" alt="Image" width=100% height =100%> |  <img alt="PaintingOverForEyeball" src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/f24ee6b1-a3f6-427e-a4c7-51f024019433" width=100% height=100% > | <img src="https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/12b5eafb-4857-44d1-afca-b55f5ca9cb57" alt="Image" width=100% height =100%>|
| As you can see, there is no eye | Paint over where you want the Eye | It creates an Eye! |

With the masking feature, you can paint over a portion of an image and provide a prompt of either the actual weapon or what you want the painted portion to be filled in with. In this example, I had an image I liked, but I wanted to add an eye ball to it. I simply painted over where I wanted the eye, and added the same image description, but I emphasised the "fiery eyes" portion with parenthases. The model then filled in the masked portion with an eyeball that looks quite good!

## Generating Sketches
#### Image Description
- This is a rought sketch of a futuristic weapon. Add details, textures, colors, and other advanced aspects.
  
| A hand drawing I made in 2 minutes (I am not a good artist 😞) | The models recreations of it |
|:-------:|:-------:|
| <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/03c2fdef-3a56-424c-b9f4-2aeaa3a3a8f8' width=35% height=35% alt=Drawing1> | <img src='https://github.com/EliBrignac/Destiny_Weapon_Maker/assets/94129362/a45824e4-30c8-4fee-8229-599ab1eb8358' width=100% height=100% alt=grid-0001> |

In this example I hand drew a weapon that I thought would be cool. I then used the img2img feture to improve this sketch, because I am not very good at drawing. Granted, not all of the generated sketches look quite like the one I drew, such as the top left and top right images, but others like the top middle look quite like what I drew. However, I do not view this variation as a bad thing, as I ended up liking the top left image the most!


# Tips and Tricks
There are a few things you should know that would help you before you jump into generating images

#### General Tips
- Adding Parenthases around words in the discriptions emphasises the words
 - Example: "(Rocket Launcher) that boasts a fierce (dragon mouth) at its tip, intricately sculpted with snarling teeth and (fiery eyes), embodying both power and mythical allure."
  - In this, we emphasised the terms "Rocket Launcher", "dragon mouth", and "fiery eyes"
- Including words like Futuristic, Detailed, Textured, 4K, HD, Advanced, etc. generally yeilds better results
- Increasing the sampling steps yeilds more high definition images and better results, although the image generation will take longer
 - I have found that 80 steps is the sweet spot where anything greater than that mark takes longer and yeilds diminishing returns

#### [Gradio UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) Functionality
- To change the shape of the images generated, use the width and height sliders
- Increasing the amount of sampling steps betters the image clarity, but increases the time to generate images (I found 80-100 is a sweet spot)
- Increasing the Batch Count increases the amount of individual images generated (Batch Count = 4 and Batch Size = 1 will generate 4 individual images)
- Increasing the Batch Size increase the amount of images generated simultaniously (Batch Count = 1 and Batch Size = 4 will generate 1 grid of 4 images)
- [CLICK HERE FOR MUCH MUCH MORE](https://github.com/AUTOMATIC1111/stable-diffusion-webui)










