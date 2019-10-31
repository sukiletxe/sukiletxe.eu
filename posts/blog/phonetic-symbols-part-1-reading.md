<!--
.. title: Phonetic symbols (part 1): reading
.. slug: phonetic-symbols-part-1-reading
.. date: 2018-06-05 14:00:00 +02:00
.. tags: accessibility, Eloquence, Espeak, IOs, JAWS, linguistics, Mac, NVDA, phonetics, Unicode, VoiceOver, Windows, IPA
.. category: 
.. link: 
.. description: 
.. type: text
-->

As an English Studies student, I've taken several courses which dealt with phonetics (Spoken English, English Phonetics, English Phonology, and some others). In these courses, I had to read and write IPA symbols. This series focuses on this topic. I will explain the alternatives and tools blind people have, along with their advantages and inconvenients. Our first part deals with reading the symbols. So, let's get started!

## Speech synthesizers

First, as these symbols are not available in every speech synthesizer, we must choose which one to use. If we are on Mac OSX or iOS, thanks to the terrific support of Unicode symbols that Apple has built into the speech synthesizer, we are good to go. If I remember correctly, there are some symbols where the speech goes silent (they have no description), but apart from that, in general the situation is better than with any other synthesizer. If we are on Windows, we have several options:

* Eloquence: With JAWS and the  NVDA addon, the situation is really bad. Most symbols produce absolutely no output.
* Espeak or Espeak NG: Comes integrated in NVDA. Includes most symbols, and if a symbol with no associated description is found, the Unicode value is said instead. In my opinion, the best alternative for Windows, despite its robotic sounding voice. 

I have no experience with other synthesizers or opeating systems. In Linux, I assume the default situation is the same as in Windows with Espeak, as Orca uses that synthesizer by default.

Despite what I said above, if you still want to use your preferred synthesizer (Eloquence, SAPI, etc.) and the IPA symbols are not supported, you could make your preferred screen reader  interpret these symbols for you (at least in Windows), by using a dictionary or a symbol table. I've found two guides for JAWS, which include already made symbol tables ([\[1\]][l1], [\[2\]][l2]). I don't use JAWS regularly, so I don't know how well they work, or how updated they are for new (or old) JAWS versions. 

[l1]: https://accessibility.psu.edu/foreignlanguages/jawssymbols/
[l2]: https://www.ruf.rice.edu/~reng/jaws-ipa.html

## Braille

I don't know much about how screen readers behave when rendering these symbols in Braille. I know that both NVDA and JAWS don't display them correctly, but they offer facilities to include Braille tables. The  links above include Braille tables for JAWS, but if you use a different Braille code for phonetic symbols (as Spanish speakers do) you are out of luck. I know that Fonos, a program to write phonetic symbols in Spanish which is included in [Uni2Bra], includes a jbt file which uses the Spanish Braille code. I will talk about this program in another post.

Regarding NVDA, I know that there exists a way to convert JBT files into NVDA compatible ones. I will investigate this and update this post when I find something. However, probably a configuration profile would be in order, as some symbols would be replaced by incorrect representations.

[Uni2Bra]: ftp://ftp.once.es/pub/utt/tiflosoftware/Miscelanea/uni2bra.zip

## Actually finding the symbols

The [official IPA chart] in pdf isn't really accessible. [Wikipedia] is a better resource for IPA. It contains descriptions of all symbols, with sample sound files. [Here is a pdf with the Unicode values associated with the symbols][unipdf]. [This is another resource for IPA and Unicode numbers][Wells]. These two files are intended to help in writing the symbols (or at least that's what I use them for).

I made [an accessible version of the 2005 update of the IPA chart][wipachart2], based off of [a less accessible one][wipachart].

[Wikipedia]: https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
[official IPA chart]: https://www.internationalphoneticassociation.org/content/full-ipa-chart
[wipachart]: https://westonruter.github.io/ipa-chart/
[wipachart2]: https://westonruter.github.io/ipa-chart/accessiblechart.html
[Wells]: https://www.phon.ucl.ac.uk/home/wells/ipa-unicode.htm
[unipdf]: https://www.internationalphoneticassociation.org/sites/default/files/phonsymbol.pdf

## When all of this fails

When all of this fails, things are out of your control. Pdf files are famous for making reading these symbols somewhat difficult, for some reason. However, it might be the case that the symbols used are old, [non-Unicode (Or PUA) symbols][Wells2]. If this is the case, and if these symbols are in a Word or Powerpoint file, copying these symbols from Powerpoint to Word might halfly solve your problem, rendering legible pseudo-IPA symbols (I instead of ɪ, for example), instead of weird symbols. This is more common if the font used in the file is IPA-SAM. I don't know why this happens.

[Wells2]: https://phonetic-blog.blogspot.com/2010/12/ban-legacy-fonts.html

---

And we've reached the end of today's post. I hope you've enjoyed it. If you have comments or questions, just drop them here, or contact me. Thanks for reading!

## Updates

* 2019-10-31: Reorganize "how to find the symbols" heading. Remove claim that Wikipedia is not accessible (which isnot true anymore).
