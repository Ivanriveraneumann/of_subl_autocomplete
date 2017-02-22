# of_subl_autocomplete
Python script to generate sublime snippets for openframeworks functions by scrapping them from OF documentation website.

<h2>(Disclaimer)</h2>
This may not be the optimal or most elegant solution to have Openframeworks autocompletion in Sublime.

<h2>Introduction</h2>
<p>
I tried to setup Openframeworks on Debian but i experienced lots of issues with IDEs: qt-creator, for some reason, had an start up problem, and i don't like Codeblocks (i don't like IDEs anyway). So i tried to make it with Sublime Text, but it also failed (running Openframeworks in Sublime it's a bit tricky in my opinion, because the documentation you can find is not really clear about how to do it, specially on linux)
</p>
<p>
Since you can create Openframeworks projects with projectGenerator and you can compile and run them with Make, is not mandatory to use an IDE such as QT, Xcode or Codeblocks, specially if you are not on OSX where you can use Xcode. So i decided to write this tiny scrapper to generate Sublime custom snippets.
</p>

<h2>How it works</h2>

<p>
<h3>Step 0</h3>
If you only need autocompletion just for the drawing module, just extract <code>ofGraphics.tar.gz</code> file, and place the ofGraphics/ folder in <code>~/.config/sublime-text-3/Packages/User/</code>.
</p>

<p>
<h3>Step 1</h3>
The script fetchs what is on the h2 tags contained in the div object with the "documentation_detail ofBackground"  css selector, and formats the scrapped text to generate the custom snippets.
</p>

<p>
In order to not bloat your system with tons of files, you have to give the script the module section you want to scrapp in order to generate the snippets you are looking for. To do so, just replace the value of the url variable at the begining of the script with the url of the module you want to scrap, for instance
</p>

<span> #default value (generates snippets for drawing functions)</span><br>
<code>url='http://openframeworks.cc/documentation/graphics/ofGraphics/'</code>

<span>#new value (generates snippets for 3d utilities)</span><br>
<code>url='http://openframeworks.cc/documentation/3d/of3dUtils/'</code>


<p>
<h3>Step 2</h3>
Once you are done step 2, just run the script as any other Python script. It will generate a folder in the script folder with the name of the module you just scrapped.
</p>

<p>
<h3>Step 3</h3>
Now just paste that folder in <code>~/.config/sublime-text-3/Packages/User/</code>. This path is where Sublime stores custom snippets files in Linux.
</p>
