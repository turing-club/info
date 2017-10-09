# Intro to Shells

If you're just getting started with coding for the first time, this article will be helpful. If you've ever installed a package on your computer via the command line, you won't need this tutorial.

## What are shells?

A shell is your computer's command line. It's basically an interface that lets you talk to your computer through text commands (just like in the olden days!) as opposed to clicking or tapping on stuff.

## Why do I need to use shells?

A lot of the coolest software and code out there doesn't come with a graphical user interface that you can interact with. In many cases, you have to feed in code and let the computer spit out the info you need. This can be done through a shell. In the case of machine learning, you might install a package defining some terms and commands for your computer. Then, for example, you'd use some of those commands to train your computer how to categorize images and label them correctly.

## OK, so how do I set all this up?

### Mac:
Go to your Applications folder. Inside that folder is a folder called Utilities. Inside that folder is an app called **Terminal**. Start it up!

Welcome to the other side of your computer. It might look a bit scary now, but don't worry! Now we're going to install a couple of useful packages: `pip` and `virtualenv`.

First, type `easy_install pip`

`pip` is a tool you'll use to install a lot of packages for your computer. Not as easy as double clicking to install, but it's not too bad.

Once this is finished, type `pip install virtualenv`

`virtualenv` is a package that lets you do all of your coding and development in a single folder, or **virtual environment**, on your computer. This is useful because:
- If you mess something up in your code, you won't mess your computer up.
- If you're working on different projects that need different software to work, you can keep them in different `virtualenvs`, which keeps stuff neat and tidy.

Now it's time to create your first `virtualenv`! Think of a catchy name for your folder, like "my_coding_stuff" (all lowercase and one word!)

Then, type `virtualenv` followed by the name you chose for your virtual environment. For example, `cd my_coding_stuff`

Awesome! Check our your virtual environment by typing `cd` followed by the name you chose for your virtual environment. On the next line, type `source bin/activate` to activate the virtual environment!

Congratulations! You can now safely code within this environment.

---
### Windows:
The first step is to install Python, a programming language that's used a lot in computer science, biology, and statistics. To get Python, go to [the Python website](https://www.python.org/downloads/release/python-363/), scroll to the bottom, and click on "Windows x86 executable installer". Then install Python as you would install any other app.

Once that's finished, search (in the Start menu or through Cortana) for an app called **PowerShell**. Start it up!

Welcome to the other side of your computer. It might look a bit scary now, but don't worry! Now we're going to install a useful package: `virtualenv`. To do so, type the following code:
```
pip install virtualenv
pip install virtualenvwrapper-powershell
Import-Module virtualenvwrapper
```

`virtualenv` is a package that lets you do all of your coding and development in a single folder, or **virtual environment**, on your computer. This is useful because:
- If you mess something up in your code, you won't mess your computer up.
- If you're working on different projects that need different software to work, you can keep them in different `virtualenvs`, which keeps stuff neat and tidy.

Now think of a cool name for your virtual environment - just make sure it's all lowercase and one word! For example, "my_coding_stuff"

Now type `New-VirtualEnvironment` followed by the name you've just thought of, for example `New-VirtualEnvironment my_coding_stuff`

Congratulations! You can now safely code within this environment. Note that unless you're prepared to change some files, you'll have to type `Import-Module virtualenvwrapper` every time before you start working in a virtual environment.

More stuff coming soon!
