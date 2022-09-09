

img1="earth2.png"
img2="note.png"

convert $img1 -fuzz 2% -transparent white $img1
convert $img2 -fuzz 2% -transparent white $img2

#magick convert $img1 $img2 -gravity Center -geometry 256x256+30+5 -composite -resize 64x64 output.png
convert $img1 $img2 -gravity Center -composite -fuzz 2% -transparent white music-earth.png
