import sys
from PIL import Image, ImageDraw
S=4  # supersample: design grid is 512, canvas 2048
def P(pts): return [(x*S,y*S) for x,y in pts]
def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
def draw(full=True):
    im=Image.new("RGBA",(512*S,512*S),(0,0,0,0)); d=ImageDraw.Draw(im)
    # frame + window
    d.rounded_rectangle([0,0,512*S-1,512*S-1],radius=56*S,fill=(27,54,88))
    d.rounded_rectangle([108*S,36*S,470*S,396*S],radius=40*S,fill=(255,255,255))
    d.rounded_rectangle([40*S,412*S,470*S,422*S],radius=4*S,fill=(150,168,188))
    # feather: left and right edges from tip to base
    L=[(432,62),(350,126),(292,170),(218,206),(168,256),(152,302),(176,348)]
    R=[(432,62),(412,116),(388,172),(354,232),(322,290),(292,334),(262,356)]
    light,mid,dark=(170,222,236),(58,134,179),(21,48,83)
    n=len(L)-1
    for i in range(n):
        t=i/(n-1)
        c1=lerp(light,mid,min(1,t*1.6)) if t<.6 else lerp(mid,dark,(t-.6)/.4)
        c2=lerp(c1,dark,.25)
        a,b,c,e=L[i],L[i+1],R[i+1],R[i]
        mx=((a[0]+e[0])/2,(a[1]+e[1])/2); my=((b[0]+c[0])/2,(b[1]+c[1])/2)
        d.polygon(P([a,b,my,mx]),fill=c1)
        d.polygon(P([mx,my,c,e]),fill=c2)
    # lower barb
    d.polygon(P([(118,408),(176,346),(214,372)]),fill=(58,134,179))
    d.polygon(P([(214,372),(176,346),(262,356)]),fill=(30,70,110))
    # nib
    d.polygon(P([(38,274),(196,290),(166,330)]),fill=(253,145,114))
    d.polygon(P([(196,290),(306,424),(166,330)]),fill=(251,196,150))
    d.line(P([(196,290),(306,424)]),fill=(214,110,90),width=3*S)
    return im
big=draw()
for size in (128,96,48):
    big.resize((size,size),Image.LANCZOS).save(f"icon-{size}px.png")
# Chrome store icon: 96 artwork centered in 128 transparent canvas
st=Image.new("RGBA",(128,128),(0,0,0,0)); st.paste(big.resize((96,96),Image.LANCZOS),(16,16)); st.save("store-icon-128.png")
big.resize((512,512),Image.LANCZOS).save("preview-512.png")
