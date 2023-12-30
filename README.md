# teporingo-bunnyadvice.com.mx
#### Video Demo:  <URL HERE>
#### Description:

Introduction about the creator (Me):
Hi, my name is Raul Chimal Hernandez and I'm a 22 years old Computer Science Student from Mexico,
I'm months apart (well half a year) from receiving my Bachelor's Degree, but you are not here to know and read about me.
Might as well continue presenting my project .... MY PROJECT: teporingo-bunnyadvice.com.mx!!!! (accessible from: https://teporingo-bunnyadvice-com.onrender.com/)

Context About Webpage: Let's start from the beginning, in CS50 we were asked to make a final project, I thought about a CV on a webpage for me or a gym webpage for myself, or ...  wait, why would I do it for myself?, yes, of course, I could do that, but do I really want to do a final project for myself instead of something for the world?, why was I being selfish with my knowledge. At that turning point I really knew 2 things: 
1.- I really wanted to do something for someone else as my project. 
2.- I doing it on Html and Css (I'm Doing a Website) 
3 (and secret).- I don't really love doing websites

Teporingo-bunnyadvice-com forged from the love and care I've experienced these last 10 years, being a bunny owner, friend, and career, I've experienced everything, from anger, stress, and sadness to joy, laughs, and love, and being "exotic pets", the negative parts of the last mentioned experiences are pretty hard.
I know there are a lot of Facebook pages, groups, webpages, and articles that talk about and cover bunny care, health, and worries.
But as I mentioned earlier, I really wanted to do something extra, so I remember a little friend I admired much more on my last visit to 
the Zoo, because of my beloved pets, the Teporingo or the Rabbit of the Volcanos
The teporingo it's an endangered species (At one point scientist and research pointed to the fact that it was Extinct) (Plot twist it wan't
it was just "not found where it should or would normally be").

The webpage as a concept not only does contain bunny info for new owners and old ones but also serves as a channel, a sign to raise
awareness about our endemic friend the Teporingo, as we must "not only take care and protect the animals we receive in our homes, we need to protect and care about the ones that are outside it and receive us in their home, the planet Earth" 


Teporingo-bunnyadvice-com from a Programmer's Perspective:
Hi! Sorry about the feelings in the last part, I'm not a computer to just compile 1's and 0's, I also compute Love
Hands down, I really expect you to enjoy this webpage that I myself created and hope you find It useful and good looking.

Let's start from the basics: 
Why a webpage? My answer: I don't really love and know how to create one, and I'm not gonna lie I thought it was simpler, guess what, it's not I really like to "put me in the spot", in this experience I do not only learn and feel more comfortable programming WebPages, but I also could appreciate well-designed pages more, learning new things, new challenges, and discover a way to quite literally say: HI WORLD! IM HERE LOOK AT THE THINGS I'M DOING, you can look them up with your phone, tablet or PC it's on the web just visit it

As for why I decided to implement Jinga and Python and not a more traditional HTML, CSS, or JavaScript: 
(Firstly, I would like to say I'm currently also working on another web project but this time using ASP.NET and W3.CSS and I think it's so much more comfortable and easier than working with app.py and bootstrap.). In a few words, the course contents make you decide between traditional HTML or Python App, and working with ASP.NET I really liked the way code shrinks and looks and acts more efficiently, so It wasn't a big decision to transition the webpage from the traditional to the python way. The best thing about its jinja and the way the HTML loads in app.py, the layout makes the code smaller, which something very importan in HTML as it tends to grow bigger and bigger in each "<div>"

Project Organization:
The folders and files in the project, follow the "traditional" or "recommended" app.py structure:
1.- static
2.- templates
3.- app.py
4.- requirements.txt

1.- STATIC:
Here I just made 4 more folders (as I like to have everything organised):
1.1- CSS
1.2.- fonts
1.3.- img
1.4.- text

1.1 Css
This folder contains the CSS for each HTML or template, and also the ones for 4 main important things:
1.1.1 Header
1.1.2. Navbar
1.1.3. Footer
1.1.4. General

Each one loads to the layout in templates, as these styles will remain and predominate in every single HTML, they are self-explanatory as each one just contains styles for the name of each file. 
As for each HTML having it's own style, I wanted to try a Jinga block in styles and also I'm not good at CSS so having a separate one for each HTML lets me work with "general classes as rows, containers, etc." in a simpler way instead of making classes with larger names or having to make an ID for each element and have them with the same style

1.2 Fonts
Here are just the files of the fonts used in the project, as i did not use library as Google Fonts, I choose to have different and "imported" fonts as an Easter Egg, as each font name it's Bunny or somehting relaated to bunnies.

1.3 img 
Folder in which I load my images, using pngs, jpgs, and SVG. I wanted to use svg more, because they maintain the same quality in every type of device and dimensions, but could not because svgs can get very heavy and complicated, making them harder not only to import but mainly to make, so I chose to use it in majority .pngs and just make the header and logo to stay in .svg to maintain the best resolution and quality in these ones 

1.4 text 
Its a .CSV with the phrases loaded in "Daily Bunny" with a format of type: Quote|Author, The character "|" was chosen as the "divisor" character as ""  (used normally), made the reader of the quotes (python reader) confused and a little harder to implement, also I wanted to try a different format and made the fetched chosen quote process easier to display,  Also I left a little "Easter Egg" in the csv DailyBunny.csv

2.- Templates 
In this folder every HTML page on my website is saved in mainly purely code, each one has Its own difficulties and errors, but the one I really struggled with is the Index, I really wanted the Index to be good, because its "the first impression of the page", so I wanted something special, (I ended up fighting for my life because of an overlay dilemma), I ended up merging the images and display them in just one, moral of the story, overlay and special orientation or behavior like a float it's hard. The real moral of the story, it's very important to first plan how would you like the page to see, be and behave, so when you code it's easier to implement, also try to keep things simple, as trying to make "cool" things, can bring more difficulties than rewards, remember that each problem-solving method has its limitations, nonetheless the thing that you really wanted maybe it's not as simple as you thought but if you could imagine it, you can code it, just that it's going to take more hours and lines of code than expected

In the app.py is where I manage the loading of each quote in Daily Quote, previously it was on javascript but in Python its easier and in fewer, lines of code, the reason I didn't make it fetch a different one "Daily" it's because i wanted the user to see that if you reload or visit again the Daily Quote page, there will be another one.

Other things I can say bout the rest of the pages, I tried to animate each one to make the page more lively added the Error 404 page
when someone messes up with the URL, and as I already said, each one has its own special thing, but I don't want to extend more

3.- app.py
Its a pretty simple and easy app.py, at the top, are the imports I need, then the call to app, each function loading each HTML, and the page that uses Python as I previously said its Daily Quote, a small Python reader to fetch the quote from the csv of quotes, it was really simple and grateful to migrate from javascript to python to load the quotes, the comparison in line of quotes it's incredible, also to import them to the html with Jinga was simpler than the traditional way of Html and Javascript.

4.-requiremnts: 
In the requirements we have the main imports that we need, I tried to implement googletrans to translate my webpage from English to Spanish, but I didn't want to use Google Translate API as it had a small test period and I didn't want that after it expired some parts of the page broke as I didn't know where and if the webpage was going to be qualified by cs50 staff

Thats pretty much a rough resume of this website, I could extend more and write in detail, but I think I covered the most important things as I also didn't want to make this very long, I know CS50 encourages you to write in detail about each part but I prevented my self to really entering in detail mainly because the language barrier (me not writing correctly or expressing myself the same way as If I'd write in Spanish, but as a matter of fact I did the whole website in English and not in Spanish, to make me practice it more) and also I think that too much detail will bore the reader.

As for extra Info I really put effort in fetching free license images, I even made one or two with AI, the only one I ended up adding its the "Mayan Teporingo".

In conclusion, I'm really happy with the results, I tend to be a perfectionist and I know that with more time, effort, and knowledge this page could turn into a 100 (right now I think it's at a 70 - 80% of what could really be), but also I learned through my programing years to appreciate my effort and not discredit or minimize the things I do, and that there is a reason why "maintenance" exist, not only to perfect your work, but improve it as the technology surrounding and inside it evolve also to let you make better, bigger and easier things, If someone asked about my favorite part of the project, I'd say that Im proud about the entire concept, I love the fact that It's a page to help bunny owners but also a little love letter for my pet bunnies, and to the teporingo, in this page, I can make it part of it, and with that I also think Im making a tribute to my roots.