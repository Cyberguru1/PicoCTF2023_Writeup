# VM0 (100 points)
<hr>

<p>The task involves a Collada file, the first step I took was to open the file in Three.js, an online emulator for 3D designs. Upon loading the file,we got this </p>
<hr>

![](files/vm0/image.png)

 <p>I noticed that the box contained two gears, and I decided to change the view to wireframe to better understand the structure of the model.</p>
 <hr>

 ![](files/vm0/image2.png)

<p>By switching to wireframe view, I was able to see the box's internal structure more clearly and identify the gears. I then proceeded to dismantle the box by removing each Lego piece in the body one by one until the gears were the only components remaining. This process allowed me to focus solely on the gears.
</p>
<hr>

![](files/vm0/Studio_Project.gif)


<p>To go into further detail, a Collada file is a type of 3D model file format that is used to represent 3D graphics in a variety of applications. Three.js is a JavaScript library that provides a simple way to create and display 3D graphics on the web. By using Three.js to load the Collada file, I was able to easily manipulate and explore the 3D model, including changing the view to wireframe mode to see the model's internal structure.</p>

<p>After dismantling the box by removing each Lego piece by piece we arrived at this.</p>
<hr>

![](files/vm0/image3.png)

The driver gear (the bigger one) has 40 teeths, while the driven gear (the smaller one) has 8 teeths. So, if the driver gear makes 1 rotation, the driven gear will make 5 rotations. If you recall we have an input we got from the file we downloaded from the task description.

```
┌──(bl4ck4non㉿bl4ck4non)-[~/Downloads/CTF/picoCTF_2023/rev_eng]
└─$ ls
input.txt
                                                                                                                                                                                                
┌──(bl4ck4non㉿bl4ck4non)-[~/Downloads/CTF/picoCTF_2023/rev_eng]
└─$ cat input.txt 
39722847074734820757600524178581224432297292490103996086521425478666370329 
```
So, if the input is the number of rotations the driver gear this means the driven gear will make 5 times the rotation of the driver gear. This means the driven gear will make ```198614235373674103788002620892906122161486462450519980432607127393331851645``` number of rotations. This number of rotations for the driven gear is actually encoded. Interesting right?😎

Lets decode this from Decimal to Hex

![image](https://user-images.githubusercontent.com/67879936/228673512-1c6a412a-7838-4d18-88df-fc41272abd3e.png)

Then we convert from Hexadecimal to Text

![image](https://user-images.githubusercontent.com/67879936/228673766-6d7ab372-bc06-4bba-b48b-8c4ba3ae38ee.png)

cool, we got our flag

------------------------------

# Ready Gladiator 0 (100 points)
<hr>

![](files/RG0/RG0.png)

<p>This challange is about the CodeWars warriror, in this task they need us to make a warrior that always loses with not ties</p>

<p>Simple solution was to send `end` to the terminal after connecting to the instance throws us back our flag!! (<_>)</p>
<hr>

![](files/RG0/Flag_RG0.png)

# Ready Gladiator 1 (200 points)
<hr>



# Reverse (100 points)
<hr>

![](files/reverse/reverse.png)

<p>This was a basic reverse engineering challenge, as usual runing strings on the file and greping for keyword `pico` gave us the flag!! (<_>)</p>

![](files/reverse/reverse_flag.png)

# Safe Opener 2 (100 points)
<hr>

![](files/safeopener/SafeOpener2.png)

<p>Doing the same operation as the previous challenge we got our flag</p>

![](files/safeopener/safeopener_Flag.png)

# timer (100 points)
<hr>

![](files/timer/timer.png)

<p>This an andriod challenge, looks simillar to the apk series in the picoGym, first thing was to unpack the apk file downloaded with <p>

# No way out (200 points)
<hr>

![](files/NoWayOut/nowayout.png)

Finaly!!, some 3D action game for reversing, this a 3D game made with Unity, downloading the file from [here](https://artifacts.picoctf.net/c/285/win.zip) and running it we have

![](files/NoWayOut/nowayout1.png)

the goal of the challenge is to Escape and get the flag

