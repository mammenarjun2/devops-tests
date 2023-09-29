# SpareRoom Docker & scripting test

This test should be completed in your own time with no time-limit. You are free to search for anything you need to complete the task via a browser. 

## Docker / scripting exercise

- This `scripting` exercise aims to accesses your ability to write scripts & use docker

- The directory `/images` contains several jpg images, a few of them visual duplicates. 

- `/bin/phash.pl` is a small Perl program that for an image passed as an argument will print a
64-bit hex string, the "perceptual hash". Duplicate images will have the same perceptual hash.

### Tasks:
- In any scripting language you wish (e.g. Bash/Python/Perl), write a script that uses the program `/bin/phash.pl` to identify (or just delete if you prefer) the duplicates in the `images` directory. If you want to do the script in Perl, you don't have to use phash.pl as a command line program, just use code from it.

- Please present your solution in a docker environment. The environment should include everything needed to run your solution.

- ***Hint***: *apart from Perl, you will need to install the perl module [Image::PHash](https://metacpan.org/dist/Image-PHash) to run the program `bin/phash.pl`. An easy way to install a parl module with its dependencies is to use a package manager like [cpanm](https://metacpan.org/pod/App::cpanminus)*