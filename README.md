### CSV Merger

<hr>

#### About

App merges two .CSV files into one. It allows user to define what files should be selected, what column to be 
merged by and what type of join should be used.

<hr>

#### Features

<ol>
<li>Validation for user input - command, files sizes, paths, name and type</li>
<li>Default inputs if no provided</li>
<li>All three merge type working</li>
<li>If no same column in both files, app ask for new ones</li>
<li>Saves output to file</li>
<li>Print result to command line</li>

</ol>

<hr>

#### Quick start

Executable path: `main_executalbe/main.exe`.

Use command `join` for a sample version.

Full command:
`join file_path file_path column_name join_type`

User enter paths to files, what column to be merged by, and what type of merging. 

Example:
`join C:\XYZ\cvs_merger\csv_files\myFile0.csv C:\XYZ\cvs_merger\csv_files\myFile1.csv id left`


App needs to have directory `../csv_files`

<hr>

#### Things to work on

<ol>
<li>Tests, tests, tests</li>
<li>Continuous working mode</li>
<li>Simplification of code</li>
<li>Better performance</li>
<li>User choice for only printing the file or only saving it</li>
</ol>   

<hr>

#### From Author

This project was a great journey and challenge. I learnt a lot and it gave me a lot of satisfaction when all one by
one started working as intended. Result code could be done with better quality, performance and even shorter.
I worked on it a lot after my current work / university, so the result code is what it is now. I plan to work on it
even after the deadline to learn even more.

Lastly, test were manual with a couple of files. Some of it can be found in repo. If I had more free time I would have
more like TDD approach.
 
<hr>
     
#### Last words
![My work](https://i.kym-cdn.com/entries/icons/original/000/028/021/work.jpg)

