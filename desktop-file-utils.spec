Summary:	Utilities for working with desktop entries
Name:		desktop-file-utils
Version:	0.21
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://freedesktop.org/Software/desktop-file-utils
Source0:	http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
BuildRequires:	popt-devel
BuildRequires:	glibc-static-devel
BuildRequires:	glib2-devel
BuildRequires:	emacs-bin

%description
desktop-file-utils contains a couple of command line utilities for working
with desktop entries. It requires GLib and popt to compile, because the
implementation requires Unicode utilities and such.

Right now the only documentation is "desktop-file-install --help".
desktop-file-validate takes a single argument, the file to validate. 

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
cat > %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el << EOF
(autoload 'desktop-entry-mode "desktop-entry-mode" "Desktop Entry mode" t)
(add-to-list 'auto-mode-alist
'("\\\\.desktop\\\\(\\\\.in\\\\)?$" . desktop-entry-mode))
(add-hook 'desktop-entry-mode-hook 'font-lock-mode)
EOF

%post
%{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null 2> /dev/null

%triggerin -- %{_datadir}/applications/*.desktop, %{_datadir}/applications/*/*.desktop
%{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null 2> /dev/null

%triggerpostun -- %{_datadir}/applications/*.desktop, %{_datadir}/applications/*/*.desktop
%{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null 2> /dev/null

%files
%doc AUTHORS NEWS README ChangeLog
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
%{_bindir}/*
%_mandir/man1/*
%{_datadir}/emacs/site-lisp/desktop-entry-mode.el*

%changelog
* Thu Mar 08 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.20-1mdv2012.0
+ Revision: 783407
- new version

* Thu Dec 29 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.19-1
+ Revision: 748193
- new version
- xz tarball

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.18-5
+ Revision: 663765
- mass rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.18-4
+ Revision: 640265
- rebuild to obsolete old packages

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 0.18-3
+ Revision: 637508
- more triggers

* Fri Feb 11 2011 Funda Wang <fwang@mandriva.org> 0.18-2
+ Revision: 637219
- convert rpm file trigger to rpm5 standard trigger

* Sat Jan 15 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.18-1
+ Revision: 631100
- update to new version 0.18

* Thu Sep 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.17-1mdv2011.0
+ Revision: 582144
- new version
- add man pages

* Mon Apr 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.16-2mdv2010.1
+ Revision: 533661
- don't print desktop entry validation warnings anymore
- update license
- remove KDE3 file trigger

* Thu Mar 11 2010 Frederic Crozat <fcrozat@mandriva.com> 0.16-1mdv2010.1
+ Revision: 518039
- Release 0.16
- Remove patch0, merged upstream

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.15-6mdv2010.0
+ Revision: 413348
- rebuild

* Sat Mar 07 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.15-5mdv2009.1
+ Revision: 350876
- Fix format string
- Fix format string

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.15-3mdv2009.0
+ Revision: 264401
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Pixel <pixel@mandriva.com> 0.15-2mdv2009.0
+ Revision: 217390
- add rpm filetrigger running update-desktop-database when rpm install/remove .desktop files

* Thu Mar 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15-1mdv2008.1
+ Revision: 180329
- new version

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2008.1
+ Revision: 149168
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 0.14-1mdv2008.0
+ Revision: 78127
- New version 0.14

* Sun Jun 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.13-1mdv2008.0
+ Revision: 40471
- drop patch 0
- spec file clean
- new version


* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-2mdv2007.0
+ Revision: 87395
- bot rebuild
- Import desktop-file-utils

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2007.1
- unpack patch
- drop patches 0,1
- fix source URL
- New version 0.12

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.11-5mdv2007.0
- Patch2: Encoding is deprecated

* Thu Jun 22 2006 Frederic Crozat <fcrozat@mandriva.com> 0.11-4mdv2007.0
- Patch1: fix typo in valid categories

* Sat Jun 10 2006 Götz Waschk <waschk@mandriva.org> 0.11-3mdv2007.0
- update the patch

* Sat Jun 10 2006 Götz Waschk <waschk@mandriva.org> 0.11-2mdv2007.0
- fix check for valid categories

* Fri Jun 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11-1mdv2007.0
- New release 0.11

* Thu Nov 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.10-2mdk
- fix buildrequires

* Wed Nov 24 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10-1mdk
- Release 0.10
- Remove patch1 (no longer needed)

* Fri Oct 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9-1mdk
- 0.9

* Wed Aug 18 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-4mdk
- fix emascs site-start script once and for all

* Wed Jul 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-3mdk
- another fix for the site-start script

* Wed Jul 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-2mdk
- arrgh, fix emacs sitestart script

* Wed Jul 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- add emacs lisp files
- buildrequires emacs
- New release 0.7

* Sat Jul 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- reenable libtoolize
- New release 0.6

* Sat Apr 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- don't run libtoolize
- add gnome-vfs2 stuff
- fix URL
- new version
