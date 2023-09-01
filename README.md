# Fine Tuned Stable Diffusion Model

## Table of Contents 
- Project Summary
- How it was Made
  - Building the Dataset
  - Fine-Tuning the model
  - Model Downloads
- Example Output Images
- Main Features and Functions
  - txt2img
  - img2img
  - masking
- Tips and Tricks
- How to use the models

# Project Summary
The goal of this project is to use AI to create concept weapon images for the game Destiny 2. I figured that the best way to accomplish this was to fine-tune a stable diffusion model on already existing destiny weapons. Being able to generate a plethora of concept images within minutes can be used to inspire the artists of Destiny 2 to help accelerate and empower their creative process. The old school way of refining ideas and crafting hand-drawn sketches can be time-consuming, often taking hours or even days to complete. In addition to this, the majority of these concept drawings end up discarded and only a select few make into the product, meaning countless hours of drawings, refinement, and ideas generation is waisted which is very inefficient. With my Destiny weapon generator models, I believe that this waisted time can be reduced by orders of magnitude. With these models, a Destiny 2 artist would be able to generate a plethora of images within seconds, with nothing but a description (Figure 1). Not only this, but you can also generate additional images based on initial images (Figure 1). Overall, the goal of this project is NOT to replace Destiny artists, but rather <u>empower</u> them by accelerating their creative process and reduce the time spent in the concept generation and concept refinement. In theory, this fine-tuned image generation should be possible for any kind of concept art, not just Destiny weapons.

⭐ All models can be downloaded from this [link](https://drive.google.com/drive/folders/1uXZrCxHdtw7Hc6jgOgNImyyd7khvxCtJ?usp=drive_link) (Note that each model is ~2.0 GBs large) ⭐

#### Figure 1
|Text Input (txt2img) | Image Input (img2img)|
|:------:|:------:|
| ↓ |  ↓ |
| Futuristic Auto Rifle with a Vibrant blue barrel and a Glowing Crystal in the middle of its body. Textured. 4K. Detailed. | <img src='readme_imgs\Img (3).png' width=150px height=150px alt=00038-2149986109> |
| Output Images | Output Images |
| ↓ | ↓ |
| <img src='readme_imgs\Img (24).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (23).png' width=100% height=100% alt=00038-2149986109> |


# How was it made

## Step 1) Building the Dataset
I was unable to find a dataset of high quality destiny images, so I decided to make my own. I found this website called [destinytracker.com](https://destinytracker.com/destiny-2/db/items/weapon) that had lots of statistics and userates of all of the weapons in destiny. When you click on a weapon, a high definition image shows up, and this large collection of images is what my dataset consits of. I used my webscrapping wizardry to collect all of these images, and I then posted them to [Kaggle.com](https://www.kaggle.com/datasets/elibrignac/destiny-2-weapon-images/settings).

## Step 2) Fine Tune Stable Diffusion
Fine Tuning powerful models, such as stable diffusion, is one of the most powerful and important abilities in this new age of Massive AI models. Being able to personalize multi million dollar AI models to do what you want allows small buisnesses and people (such as myself) to create things that would otherwise be impossible to create.

In order to fine-tune this model, I used a google colab T4 GPU and [DreamBooth](https://github.com/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) ([Paper Here](https://arxiv.org/pdf/2208.12242.pdf). Training over all of the images for 3000 epochs took around 40 minutes. I saved the model at 1000, 2000, and 3000 epochs and all models can be found on hugging face to be locally downloaded and used. Visit the DreamBooth link for a colab notebook that can walk you through how to use the models. Interaction with the model is through [Gradio Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui), where there are <u>TONS</u> of parameters that you can play with or read more about [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui). The things that I found to be most helpful are listed at the bottom of this README in the Tips and Tricks section. I do reccommend looking into all of the functionality of the Gradio UI because it truly is very impressive.



#### Training Image Examples
| <img src='readme_imgs\Img (5).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (11).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (12).png' width=100% height=100% alt=00038-2149986109> |<img src='readme_imgs\Img (9).png' width=100% height=100% alt=00038-2149986109>  |
|:-------:|:-------:|:-------:|:-------: |
| <img src='readme_imgs\Img (10).png' width=100% height=100% alt=00038-2149986109>  | <img src='readme_imgs\Img (6).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (8).png' width=100% height=100% alt=00038-2149986109>  | <img src='readme_imgs\Img (7).png' width=100% height=100% alt=00038-2149986109>   |   


#### Model Ouput Examples (Various Prompts)
| <img src='readme_imgs\Img (13).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (14).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (15).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (16).png' width=100% height=100% alt=00038-2149986109> |
|:-------:|:-------:|:-------:|:-------: |
 | <img src='readme_imgs\Img (20).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (19).png' width=100% height=100% alt=00038-2149986109> |<img src='readme_imgs\Img (17).png' width=100% height=100% alt=00038-2149986109> | <img src='readme_imgs\Img (18).png' width=100% height=100% alt=00038-2149986109> |


# Main Features and Functions

## Txt2Img

The Txt2Img feature was alluded to in column 1 of <u>Figure 1</u> and is likely the most intuitive feature. Txt2Img is where you give the model a description and it generates images based on that description. This feature is very helpful when you have a description of a Destiny weapon design and want some images that match it. An example below is provided.

| Description | The models output |
|:-------:|:-------:|
| Hand Cannon with Green Scales. Textured. Detailed. Futuristic. |  <img src='readme_imgs\Img (2).png' width=35% height=35% alt=Drawing1>  |


## Img2Img

The Img2Img feature was alluded to in column 2 of <u>Figure 1</u> and is super helpful for slight tweeks of designs. With img2img, you can give the model and image and give it an optional description, and the model will make slight additions and modifications to the design. This is SUPER useful if you have a design that you like, or a style you want to work with. You can also upload pictures that you drew yourself, and get images that are simlar to them like in the example below.

#### Image Description
- This is a rought sketch of a futuristic weapon. Add details, textures, colors, and other advanced aspects.
  
| A hand drawing I made in 2 minutes (I am not a good artist 😞) | The models recreations of it |
|:-------:|:-------:|
| <img src='readme_imgs\Img (21).png' width=35% height=35% alt=Drawing1> | <img src='readme_imgs\Img (22).png' width=100% height=100% alt=grid-0001> |

In this example I hand drew a weapon that I thought would be cool. I then used the img2img feture to improve this sketch, because I am not very good at drawing. Granted, not all of the generated sketches look quite like the one I drew, such as the top left and top right images, but others like the top middle are very similar to what I drew. This could be in part due to my drawing being poor, however, I do not view this variation as a bad thing, as I ended up liking the top left image much more than my original image!


## Masking
#### Image Description

- Rocket Launcher that boasts a fierce dragon mouth at its tip, intricately sculpted with snarling teeth and fiery eyes, embodying both power and mythical allure.

| Image 1                 | Image 2                 | Image 3                 |
|:-----------------------:|:-----------------------:|:-----------------------:|
|<img src="readme_imgs\Img (25).png" alt="Image" width=100% height =100%> |  <img width="90%" height=90% alt="PaintingOverForEyeball2" src="readme_imgs\Img (27).png"> | <img src="readme_imgs\Img (26).png" alt="Image" width=100% height =100%>|
| As you can see, there is no eye | Paint over where you want the Eye | It creates an Eye! |

With the masking feature, you can paint over a portion of an image and provide a prompt of either the actual weapon description or what you want the painted portion to be filled in with. In this example, I had an image I liked, but I wanted to add an eye ball to it. I simply painted over where I wanted the eye, and added the same image description, but I emphasised the "fiery eyes" portion with parenthases (See Tips and Tricks). The model then filled in the masked portion with an eyeball that looks quite good!

# Tips and Tricks
There are a few things you should know that would help you before you jump into generating images

#### General Tips
- Adding Parenthases around words in the discriptions emphasises the words
   - Example: "(Rocket Launcher) that boasts a fierce (dragon mouth) at its tip, intricately sculpted with snarling teeth and (fiery eyes), embodying both power and mythical allure."
      - In this, we emphasised the terms "Rocket Launcher", "dragon mouth", and "fiery eyes"
- Including words like Futuristic, Detailed, Textured, 4K, HD, Advanced, etc. generally yeilds better results
- A Better description of what you want will yeild better results.
- Increasing the sampling steps yeilds more high definition images and better results, although the image generation will take longer
   - I have found that 80 steps is the sweet spot where anything greater than that mark takes longer and yeilds diminishing returns

#### [Gradio Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) Functionality
- To change the shape of the images generated, use the width and height sliders
- Increasing the amount of sampling steps betters the image clarity, but increases the time to generate images (I found 80-100 is a sweet spot)
- Increasing the Batch Count increases the amount of individual images generated (Batch Count = 4 and Batch Size = 1 will generate 4 individual images)
- Increasing the Batch Size increase the amount of images generated simultaniously (Batch Count = 1 and Batch Size = 4 will generate 1 grid of 4 images)
- [CLICK HERE FOR MUCH MUCH MORE](https://github.com/AUTOMATIC1111/stable-diffusion-webui)


# How to use the models
1. Visit this link to download a model of your choice (Note each model is ~2.0 GB large)
    - Save this model to your google drive, or be prepared to upload it to Google Colab
2. Click this [link](https://drive.google.com/file/d/14cUXO97gs2bhe-OdmhJhXItAQjJLKW-u/view?usp=drive_link) to enter the Google Colab
    - Run the first 2 cells
    - Check the "Use_Custom_Path" checkbox in the third cell
    - Run the third Cell
3. Soon a box will pop up and you will be prompted to enter the path to where the model is saved. Enter the model path and press the "Enter" key.
4. Soon a URL will be generated, click it to open the Gradio UI and play with the model!







