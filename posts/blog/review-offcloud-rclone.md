<!--
.. title: Review of Offcloud and Rclone
.. slug: review-offcloud-rclone
.. date: 2018-04-01 12:00:00+02:00
.. tags: cloud, offcloud, rclone, review, dropbox, onedrive, google drive, torrent, magnet, ftp, rclone, cli
.. category: 
.. link: 
.. description: 
.. type: text
-->

## Introduction

A couple of months ago, as my ~640GB (~598 GiB) external drive stopped working, I decided to buy some space in the cloud. After several days of investigation, I decided to purchase the premium package on [Onedrive] (1TiB for 69€/year). After doing this, soon I realised that an external drive was better because of my internet speed (I have a ~3Mb download speed and ~1Mb upload speed). But, seeing as my external drive had stopped working because I dropped it to the floor by accident, I didn't want to buy one. So, what were my options? Was there a service which allowed me to download things directly to the cloud?
[Onedrive]: https://onedrive.live.com

## Offcloud

[Offcloud] is a service which lets you do three things:
[Offcloud]: https://offcloud.com
* Download things using it as a proxy ("Instant downloading)";
* Save things temporarily in its  cloud ("Cloud backup"); and
* Download things to one of your storage cloud services (Dropbox, Onedrive, Google Drive...) or through FTP or WebDAV ("Remote upload").

But wait, let's be more specific about these "things". These include:

* Direct links and webpages (webpages can be downloaded as html or pdf)
* Videos and files from several cloud storage services (both free and paid) ([list of supported sites])
* Torrent files and magnet links
* .nzb files
[list of supported sites]: https://offcloud.com/#/sites
The system is pretty simple. You paste a link or upload a torrent or .nzb file, choose your download method, and wait until it finishes. Then, you can delete the entry (and file, if it's in Offcloud's cloud), or re-download it somewhere else. It lets you download three links for free per month. If that's not enough for you, you can purchase unlimited links for a month or for a year, or purchase just some links. It has an API which lets you add links to it from other applications,  it has plugins for download managers and browsers, and it works with [IFTTT] and [Zapier]. And of course, the downloads to its cloud or to your  cloud storage service work even if you turn off your computer.
[IFTTT]: https://ifttt.com
[Zapier]: https://zapier.com
[Sign up to Offcloud](https://offcloud.com/?=9ee9276b) ([non-ref](https://offcloud.com))

So, this is great. Now I can upload things directly to my cloud, at a much faster speed than using my home connection. But my computer space is quite limited (I have a ~103GiB SSD), so I cannot download many files there if I need to transfer them to, say, a thumb drive. Luckily, there is a piece of software for solving that, too.

## Rclone

[Rclone] lets you manage your cloud services without needing to synchronize them to your hard drive, or to open a browser. This includes:

* Transferring files and folders between cloud services, or between a service's directories;
* Transferring files and folders between your computer (or any device connected to it) and the cloud;
* Renaming and deleting files from the cloud without downloading anything; and
* Accessing a cloud drive via http, WebDAV or Fuse.

It lets you apply filters for managing files or folders, so you don't need to remember long names (I use them exclusively for this), or to filter based on other criteria. It is used from the command line, and it's available for Windows, Linux and Mac. And it's free and open source.

[Rclone]: https://rclone.org/

## Conclusion

This is the setup I use now: I download one or more files using [Offcloud] to [Onedrive], and then copy it to a USB thumb drive (which, you will agree, is much less prone to fall) using [Rclone]. And, in the meantime, I save disk space and bandwidth.
