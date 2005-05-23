Name: fedora-logos
Summary: Red Hat-related icons and pictures.
Version: 1.1.31
Release: 1
Group: System Environment/Base
Source0: fedora-logos-%{version}.tar.bz2
License: Copyright © 1999-2004 Red Hat, Inc.  All rights reserved.
BuildRoot: %{_tmppath}/%{name}-root
BuildArchitectures: noarch
Obsoletes: redhat-logos
Provides: redhat-logos
Provides: system-logos
conflicts: kdebase <= 3.1.5
Conflicts: anaconda-images <= 10

%description
The fedora-logos package (the "Packages") contain image files which
incorporate the Fedora trademark and the RPM logo (the "Marks").
The Marks are trademarks or registered trademarks of Red Hat, Inc.
in the United States and other countries and are used by permission.

See the included COPYING file for information on copying and
redistribution.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
for i in redhat-pixmaps/*; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
done
(cd $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat; \
for i in *-mini.xpm; do \
  linkfile=`echo $i | sed -e "s/\(.*\)-mini/mini-\1/"` ; \
  ln -s $i $linkfile ; \
done)

# should be ifarch i386
mkdir -p $RPM_BUILD_ROOT/boot/grub
install -m 644 bootloader/grub-splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
for i in firstboot/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/rhgb
for i in rhgb/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/rhgb
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/BlueCurve
for i in kde-splash/BlueCurve/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/BlueCurve
done

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
#for i in pixmaps/* ; do
#  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
#done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bluecurve
for i in gdm/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bluecurve
done

# kdmtheme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/Bluecurve
pushd $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/Bluecurve
ln -s ../../../../gdm/themes/Bluecurve/rh_logo-header.png .
ln -s ../../../../gdm/themes/Bluecurve/screenshot.png
popd

ln -s ../../firstboot/pixmaps/shadowman-round-48.png \
 $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat/

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING
%{_datadir}/firstboot
%{_datadir}/apps/ksplash/Themes/BlueCurve
%{_datadir}/pixmaps
%{_datadir}/gdm
%{_datadir}/apps/kdm/themes/Bluecurve
%{_datadir}/rhgb
%{_datadir}/anaconda/pixmaps/*
/usr/lib/anaconda-runtime/boot/*png
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
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
