Name: fedora-logos
Summary: Fedora-related icons and pictures
Version: 9.0.0
Release: 2%{?dist}
Group: System Environment/Base
Source0: fedora-logos-%{version}.tar.bz2
# fixed KDE splash screen background
Source1: background.png

# The trademarks contained in this file are the property of Red Hat, Inc.  No
# license to these trademarks is provided or is necessary if you merely
# replicate the Fedora code as you downloaded it from the Fedora Project
# website.  However, there are permissions granted for the use of these marks
# under certain other conditions.  You may find those permissions at
# http://fedoraproject.org/wiki/Legal/TrademarkGuidelines and COPYING file.
License:  Not licensed.  See COPYING file for trademark permission.

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Obsoletes: redhat-logos
Provides: redhat-logos = %{version}-%{release}
Provides: system-logos = %{version}-%{release}
Conflicts: kdebase <= 3.1.5
Conflicts: anaconda-images <= 10
Conflicts: redhat-artwork <= 5.0.5
Requires(post): coreutils

%description
The fedora-logos package contains image files which incorporate the 
Fedora trademark and the RPM logo (the "Marks").
The Marks are trademarks or registered trademarks of Red Hat, Inc.
in the United States and other countries and are used by permission.

See the included COPYING file for information on copying and
redistribution.

%prep
%setup -q
cp -pf %{SOURCE1} kde-splash/FedoraWaves/1600x1200/background.png

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
for i in redhat-pixmaps/*; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
done
(cd $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat; \
for i in *-mini.xpm; do \
  linkfile=`echo $i | sed -e "s/\(.*\)-mini/mini-\1/"` ; \
  ln -s $i $linkfile ; \
done)

# should be ifarch i386
mkdir -p $RPM_BUILD_ROOT/boot/grub
install -p -m 644 -D bootloader/grub-splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-waves
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-waves
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/rhgb
for i in rhgb/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/rhgb
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver
for i in gnome-screensaver/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/screensavers
for i in applications/screensavers/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/applications/screensavers
done

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images
#for i in backgrounds/images/* ; do
#  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/images
#done
#
#mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties
#for i in backgrounds/*.xml ; do
#  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties
#done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/kde4/apps/ksplash/Themes/FedoraWaves/1600x1200
for i in kde-splash/FedoraWaves/{Theme.rc,Preview.png} ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/kde4/apps/ksplash/Themes/FedoraWaves
done
for i in kde-splash/FedoraWaves/1600x1200/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/kde4/apps/ksplash/Themes/FedoraWaves/1600x1200
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

for size in 16x16 24x24 32x32 36x36 48x48 96x96 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
    pushd $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/$size/apps
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png icon-panel-menu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png gnome-main-menu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png kmenu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png start-here.png
    popd
  done
done

ln -s ../../firstboot/pixmaps/shadowman-round-48.png \
 $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat/

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

for i in 16 24 32 36 48 96; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/${i}x${i}/places
  # why not use (sym)links like Bluecurve above?  -- Rex
  install -p -m 644 -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/fedora-logo-icon.png $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/${i}x${i}/places/start-here.png
  install -p -m 644 -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/fedora-logo-icon.png $RPM_BUILD_ROOT%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/${i}x${i}/places/start-here.png 
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_datadir}/icons/Bluecurve || :
touch --no-create %{_datadir}/icons/Fedora || :
touch --no-create %{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE ||:
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  if [ -f %{_datadir}/icons/hicolor/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
  fi
  if [ -f %{_datadir}/icons/Bluecurve/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/Bluecurve || :
  fi
  if [ -f %{_datadir}/icons/Fedora/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/Fedora || :
  fi
fi

%files
%defattr(-, root, root)
%doc COPYING
%{_datadir}/firstboot/themes/fedora-waves
%{_datadir}/kde4/apps/ksplash/Themes/*
%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/*/places/*
%{_datadir}/pixmaps/*
%{_datadir}/rhgb/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/Bluecurve/*/apps/*
%{_datadir}/icons/Fedora/*/places/*
%{_datadir}/gnome-screensaver/*
%{_datadir}/applications/screensavers/*
#%{_datadir}/backgrounds/images/*
#%{_datadir}/gnome-background-properties/*.xml
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%{_datadir}/icons/Bluecurve
%{_datadir}/icons/hicolor
/usr/lib/anaconda-runtime/boot/*png
/usr/lib/anaconda-runtime/*.sh
/usr/lib/anaconda-runtime/*.jpg
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
* Mon Apr 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9.0.0-2
- use bg image without rounded corners for kde-splash (Pavel Shevchuk, #443308)

* Fri Apr 11 2008 Ray Strode <rstrode@redhat.com> - 9.0.0-1
- update grub splash screen to not have sulfur and look better
  on EFI systems

* Thu Apr 10 2008 Rex Dieter <rdieter@fedoraproject.org> - 8.99.2-2
- kde-splash: rename to FedoraWaves, fixup animation
- include start-here icons for Fedora-KDE icon theme

* Wed Apr  2 2008 Ray Strode <rstrode@redhat.com> - 8.99.2-1
- firstboot changed artwork locations

* Tue Apr  1 2008 Ray Strode <rstrode@redhat.com> - 8.99.1-1
- Add grub, firstboot and anaconda artwork
- merge kde artwork from downstream
- drop unused images

* Tue Apr  1 2008 Ray Strode <rstrode@redhat.com> - 8.99.0-1
- Add F-9 rhgb artwork

* Thu Mar 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.0.3-4
- Include Waves KSplash theme for KDE 4

* Thu Mar 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.0.3-3
- Don't ship KDE 3 KSplash and KDM themes (which don't work in KDE 4)

* Fri Mar 21 2008 Matthias Clasen <mclasen@redhat.com> - 8.0.3-2
- Don't ship parts of gdm themes that gdm doesn't use anymore

* Wed Nov 14 2007 Ray Strode <rstrode@redhat.com> - 8.0.3-1
- Install Fedora Flying High GDM logo (woops, bug 382281)

* Mon Oct 29 2007 Matthias Clasen <mclasen@redhat.com> - 8.0.2-2
- Fix a typo in the description (Stepan Kasal)

* Mon Oct 29 2007 Matthias Clasen <mclasen@redhat.com> - 8.0.2-1
- Add Infinity splash screens for KDE and Gnome

* Fri Oct 19 2007 Matthias Clasen <mclasen@redhat.com> - 8.0.0-2
- Silence %%post (#340551)

* Wed Oct 17 2007 Ray Strode <rstrode@redhat.com> - 8.0.0-1
- Drop Fedora Infinity gdm theme

* Tue Oct 16 2007 Ray Strode <rstrode@redhat.com> - 7.96.0-1
- Fix up some %%install goo
- drop bluecurve kdm fedora logo images too

* Tue Oct 16 2007 Ray Strode <rstrode@redhat.com> - 7.95.0-1
- actually drop bluecurve gdm fedora logo images that aren't trademarked

* Wed Oct 10 2007 Ray Strode <rstrode@redhat.com> - 7.94.0-1
- drop bluecurve gdm fedora logo images that aren't trademarked

* Wed Oct 10 2007 Ray Strode <rstrode@redhat.com> - 7.93.0-1
- Install fedora 7 logo in the right place

* Wed Sep 19 2007 Matthias Clasen <mclasen@redhat.com> - 7.92.4-1
- Acutally install the gdm theme

* Wed Sep 19 2007 Matthias Clasen <mclasen@redhat.com> - 7.92.3-1
- Add infinity gdm theme

* Wed Sep 19 2007 Matthias Clasen <mclasen@redhat.com> - 7.92.2-1
- Add infinity lock dialog

* Thu Sep 13 2007 Bill Nottingham <notting@redhat.com> - 7.92.1-1
- add the powered-by logo (#250676)

* Wed Sep  5 2007 Jeremy Katz <katzj@redhat.com> - 7.92.0-4
- merge back changes that got lost

* Fri Aug 31 2007 Jeremy Katz <katzj@redhat.com> - 7.92.0-3
- fix grub splash image to be an actual image

* Tue Aug 28 2007 Máirín Duffy <duffy@redhat.com> - 7.92.0-1
- update the anaconda artwork
- changed default backgrounds

* Mon Aug 27 2007 Ray Strode <rstrode@redhat.com> - 7.90.2-1
- update the firstboot artwork
- update the grub artwork

* Mon Aug 27 2007 Ray Strode <rstrode@redhat.com> - 7.90.1-1
- update the rhgb artwork

* Fri Aug 24 2007 Ray Strode <rstrode@redhat.com> - 7.90.0-1
- add a 150px variant of the fedora logo
  (requested by Paul Frields)
- update license field to be more clear

* Wed Jul 04 2007 Florian La Roche <laroche@redhat.com> 6.0.98-5
- require coreutils for the %%post script

* Fri Jun 15 2007 Adam Jackson <ajax@redhat.com> 6.0.98-4
- Remove the Requires on redhat-artwork and fedora-icon-theme, and just
  multi-own the directories.  Fixes some hilarious dependency chains.

* Mon Apr 23 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.98-3
- Clean up %%post scriptlet (#237428)

* Fri Apr 20 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.98-2
- Add a Fedora icon theme

* Thu Apr 05 2007 Than Ngo <than@redhat.com> - 6.0.98-1
- fix ksplash BlueCurve theme

* Wed Mar 28 2007 Matthias Clasen <mclasen@redhat.com> 6.0.97-2
- Save some space by linking backgrounds

* Thu Mar 22 2007 Than Ngo <than@redhat.com> 6.0.97-1
- Add new Ksplash theme for Fedora 7

* Tue Mar 20 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.96-1
- Add dual screen backgrounds

* Thu Mar 15 2007 Ray Strode <rstrode@redhat.com> - 6.0.95-1
- Drop weird gnome-logo-icon-transparent.png symlink that 
  makes fedora show up where gnome logo is supposed to

* Thu Mar 15 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.94-1
- Retouch parts of the rhgb image to align it
  better with the login screen

* Fri Feb 23 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.93-1
- New backgrounds (dual versions still missing)

* Fri Feb 23 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.92-5
- Directory ownership fixes

* Thu Feb 22 2007 Jeremy Katz <katzj@redhat.com> - 6.0.92-4
- resave the syslinux splash so that it works (lalalala....)

* Thu Feb 22 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.92-3
- Improve the branded lock dialog 

* Wed Feb 21 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.92-2
- Some more new images

* Wed Feb 21 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.92-1
- New lock dialog

* Tue Feb 20 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.91-3
- Some more new anaconda images
- Slight update to one rhgb image

* Sun Feb 18 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.91-2
- Add new gnome splash 
- New firstboot images
- Add some new anaconda images
- Add new grub image

* Sun Feb 18 2007 Matthias Clasen <mclasen@redhat.com> - 6.0.91-1
- Add new RHGB images

* Thu Jan 18 2007 Jeremy Katz <katzj@redhat.com> - 6.0.90-1
- add syslinux splash for use with graphical menu

* Fri Sep 22 2006 Than Ngo <than@redhat.com> - 6.0.6-1
- add FedoraDNA theme for KDM

* Fri Sep 22 2006 Matthias Clasen <mclasen@redhat.com> - 6.0.5-1
- Add a description for the default backgrounds

* Fri Sep 22 2006 Ray Strode <rstrode@redhat.com> - 6.0.2-1
- update screenshot in FedoraDNA theme

* Fri Sep 22 2006 Than Ngo <than@redhat.com> - 6.0.1-1
- update kde ksplash

* Fri Sep 22 2006 Ray Strode <rstrode@redhat.com> - 6.0.0-1
- drop unused n-small image in FedoraDNA gdm theme
- rename fedora.png to logo.png in FedoraDNA gdm theme
- crop fedora.png to not have uneven padding in FedoraDNA 
  gdm theme

* Fri Sep 22 2006 Bill Nottingham <notting@redhat.com>
- update grub splash (#207637)

* Thu Sep 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.55-1
- Final update for FC6 graphics

* Wed Sep 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.54-1
- Update to themed lock dialog

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.53-1
- Update the syslinux splash

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.52-1
- Fix the colors in the grub splash

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.51-1
- Add new gdm theme 

* Wed Sep 06 2006 John (J5) Palmieri <johnp@redhat.com> - 1.1.50-1
- cvs add the new backgrounds this time

* Tue Sep 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.1.49-1
- New graphics for fc6
- Remove the 4:3 background and add 5:4 ratio background

* Sun Aug 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.48-1.fc6
- Update lock dialog to work with current gnome-screensaver

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.1.47-2.fc6
- Add links for new icon name used in the gnome-panel menubar

* Fri Jul 28 2006 John (J5) Palmieri <johnp@redhat.com> - 1.1.47-1
- Add a 4:3 aspect ratio background 
- Fix extention to be .jpg on backgrounds 

* Thu Jul 27 2006 John (J5) Palmieri <johnp@redhat.com> - 1.1.46-1
- Add new default backgrounds

* Wed Jul 26 2006 Alexander Larsson <alexl@redhat.com> - 1.1.45-1
- Add wide version of default desktop background

* Tue Jul 25 2006 Florian La Roche <laroche@redhat.com>
- add version/release to the Provides: in the specfile

* Tue Jul 11 2006 Matthias Clasen <mclasen@redhat.com> 1.1.44-1
- Move the complete lock dialog theme here

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> 1.1.43-1
- Add branded desktop background and move the lock dialog
  background to the right directory

* Tue Feb 28 2006 Matthias Clasen <mclasen@redhat.com> 1.1.42-1
- New artwork for gdm, kdm Bluecurve from Diana Fong

* Wed Jan 25 2006 Chris Lumens <clumens@redhat.com> 1.1.41-1
- New artwork for firstboot from dfong (#178106).

* Fri Jan 20 2006 Ray Strode <rstrode@redhat.com> - 1.1.40-1
- update the logo in the corner

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> - 1.1.39-1
- give rhgb a new look from Diana Fong

* Tue Jan 17 2006 Ray Strode <rstrode@redhat.com> - 1.1.38-1
- add logo bits of new gdm theme

* Tue Dec 20 2005 Ray Strode <rstrode@redhat.com> - 1.1.37-1
- another new image from dfong (splash screen)
- move screensaver lock dialog background here

* Tue Dec 20 2005 Ray Strode <rstrode@redhat.com> - 1.1.36-1
- another new image from dfong (screensaver sprite)

* Mon Dec 19 2005 Jeremy Katz <katzj@redhat.com> - 1.1.35-1
- new images from dfong

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 John (J5) Palmieri <johnp@redhat.com> - 1.1.34-1
- Symlink fedora-logo-icon into Bluecurve instead of hicolor
  to avoid conflicts with other packages

* Thu Nov 10 2005 John (J5) Palmieri <johnp@redhat.com> - 1.1.33-1
- Add symlinks for the panel icons to be the fedora logos

* Thu Nov 10 2005 John (J5) Palmieri <johnp@redhat.com> - 1.1.32-1
- Add new fedora logos to pixmap and icons/hicolor

* Mon May 23 2005 Jeremy Katz <katzj@redhat.com> - 1.1.31-1
- copyright date on anaconda splash (#153964)

* Mon Apr 18 2005 Than Ngo <than@redhat.com> 1.1.30-1
- add missing fedora logos for kdmtheme

* Tue Oct 26 2004 Jeremy Katz <katzj@redhat.com> - 1.1.29-1
- non-test anaconda splash

* Tue Oct 26 2004 Jeremy Katz <katzj@redhat.com> - 1.1.28-1
- generic Fedora Core graphics for !test release

* Thu Sep 30 2004 Than Ngo <than@redhat.com> 1.1.27-1
- fix kde splash

* Sat Jun  5 2004 Jeremy Katz <katzj@redhat.com> - 1.1.26-1
- provide: system-logos

* Thu Jun  3 2004 Jeremy Katz <katzj@redhat.com> - 1.1.25-1
- add anaconda bits with fedora logos

* Wed May  5 2004 Jeremy Katz <katzj@redhat.com> - 1.1.24-1
- newer grub image for fc2

* Tue Mar 23 2004 Alexander Larsson <alexl@redhat.com> 1.1.23-1
- Use correct gdm logo 

* Tue Mar 23 2004 Alexander Larsson <alexl@redhat.com> 1.1.22-1
- fix up gdm logo and add screenshot

* Tue Feb  3 2004 Jonathan Blandford <jrb@redhat.com> 1.1.21-1
- add rhgb logo

* Tue Nov 11 2003 Than Ngo <than@redhat.com> 1.1.20.2-1
- added Preview for ksplash

* Mon Nov 10 2003 Than Ngo <than@redhat.com> 1.1.20.1-1
- added new BlueCurve Ksplash Theme for KDE 3.2

* Thu Oct 30 2003 Havoc Pennington <hp@redhat.com> 1.1.20-1
- build new stuff from garrett

* Thu Oct  9 2003 Bill Nottingham <notting@redhat.com> 1.1.19-1
- add a symlink for up2date

* Tue Oct  7 2003 Bill Nottingham <notting@redhat.com> 1.1.18-1
- rename package

* Wed Sep 24 2003 Bill Nottingham <notting@redhat.com> 1.1.17-1
- new license

* Tue Sep 23 2003 Michael Fulbright <msf@redhat.com> 1.1.16-1
- added Fedora graphics

* Fri Jul 18 2003 Havoc Pennington <hp@redhat.com> 1.1.15-1
- build new stuff from garrett

* Wed Feb 26 2003 Havoc Pennington <hp@redhat.com> 1.1.14-1
- build new stuff in cvs

* Mon Feb 24 2003 Jeremy Katz <katzj@redhat.com> 1.1.12-1
- updated again
- actually update the grub splash

* Fri Feb 21 2003 Jeremy Katz <katzj@redhat.com> 1.1.11-1
- updated splash screens from Garrett

* Tue Feb 18 2003 Havoc Pennington <hp@redhat.com> 1.1.10-1
- move in a logo from gdm theme #84543

* Mon Feb  3 2003 Havoc Pennington <hp@redhat.com> 1.1.9-1
- rebuild

* Wed Jan 15 2003 Brent Fox <bfox@redhat.com> 1.1.8-1
- rebuild for completeness

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Thu Sep  5 2002 Havoc Pennington <hp@redhat.com>
- add firstboot images to makefile/specfile
- add /usr/share/pixmaps stuff
- add splash screen images
- add COPYING

* Thu Sep  5 2002 Jeremy Katz <katzj@redhat.com>
- add boot loader images

* Thu Sep  5 2002 Havoc Pennington <hp@redhat.com>
- move package to CVS

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Add a shadowman-only derived from redhat-transparent.png

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 31 2001 Owen Taylor <otaylor@redhat.com>
- Fix alpha channel in redhat-transparent.png

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Add %defattr

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Add version of logo for embossing on the desktop

* Tue May 16 2000 Preston Brown <pbrown@redhat.com>
- add black and white version of our logo (for screensaver).

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild for new description.

* Fri Sep 25 1999 Bill Nottingham <notting@redhat.com>
- different.

* Mon Sep 13 1999 Preston Brown <pbrown@redhat.com>
- added transparent mini and 32x32 round icons

* Sat Apr 10 1999 Michael Fulbright <drmike@redhat.com>
- added rhad logos

* Thu Apr 08 1999 Bill Nottingham <notting@redhat.com>
- added smaller redhat logo for use on web page

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- added transparent large redhat logo

* Tue Apr 06 1999 Bill Nottingham <notting@redhat.com>
- added mini-* links to make AnotherLevel happy

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- added copyright

* Tue Mar 30 1999 Michael Fulbright <drmike@redhat.com>
- added 48 pixel rounded logo image for gmc use

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- package created
