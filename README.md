# ip-addresses
Collector of external IP address


# Facebook Messenger Word Cloud
Create Facebook Messenger Word Cloud based on the messeges exported from Facebook archive. Script extracts messages from one or multiple `message_x.HTML` files for a selected folder and transform into `.PNG` (Word Cloud) and `.CSV` (descending words list) containing most frequently used words.
If you don't have any of the imported library, you can easily install them by coping the comment from the begining of the script `pip install XXX`. Generating a word cloud from a JSON file would probably be much simpler however, not everyone downloads this file as an archive at the first place and it wouldn't be such a challenge.

## Table of contents
* [Example Usage](#Example-Usage)
* [Custom shape](#Custom-shape)
* [Downloading messages files](#Downloading-messages-files)
* [License](#License)

## Example Usage
Generate rectangular word cloud just providing the folder path containing the `.html` files:
```
fb_word_cloud.py -p C:\fb\messages\inbox\username_xzdsmlmbaiw\
```
<img src="./images/WordCloud_rec.png" width="450" />

Generate rectangular Word Cloud without specified words:
```
fb_word_cloud.py -p C:\fb\messages\inbox\username\ -e a,in,an,or,and,how,why 
```

Generate Word Cloud in different shapes (see [Custom shape](#Custom-shape) ) without specified words :
```
fb_word_cloud.py -p C:\fb\messages\inbox\username\ -e a,in,an,or,and,how,why -i C:\Users\Desktop\like.jpg
```

## Custom shape
In order to create Word Cloud in various shapes, mask need to be provided in in a certain way. Script accepts only files with `.jpg`, `.jpeg` and `.png` extensions. Additionally, file need to have black `#000000` shape and white `#FFFFFF` background. For .png files background can be transparent.
<p float="left">
  <img src="./images/like.jpg" width="400">   </img>
  <img src="./images/WordCloud.png" width="400" />
</p>

## Downloading messages files
If you don't know how to download facebook archive, below you can find step by step manual.

1. Click on you profile picture and select **Setting & Privacy** ⮕ **Settings**
<p float="left">
  <img src="./images/facebook1.png" width="250">  ⮕  </img>
  <img src="./images/facebook2.png" width="250" />
</p>
<br/>

2. On the left side of the screen click **Privacy** tab and then **Your Facebook information**
<p float="left">
  <img src="./images/facebook3.png" width="250">  ⮕  </img>
  <img src="./images/facebook4.png" width="250" />
</p>
<br/>

3. You will have a list of options to choose from, please select **Download profile information**
<img src="./images/facebook5.png" width="800" />
<br/>
