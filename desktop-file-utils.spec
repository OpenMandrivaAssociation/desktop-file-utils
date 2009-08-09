Summary:	Utilities for working with desktop entries
Name:		desktop-file-utils
Version:	0.15
Release:	%mkrel 6
License:	GPL
Group:		Graphical desktop/Other
Url: 		http://freedesktop.org/Software/desktop-file-utils
Source:		http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
Patch0:     desktop-file-utils-0.15-fix-format.patch
Buildrequires:	popt-devel glibc-static-devel 
BuildRequires:	glib2-devel
BuildRequires:	emacs-bin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
desktop-file-utils contains a couple of command line utilities for working
with desktop entries. It requires GLib and popt to compile, because the
implementation requires Unicode utilities and such.

Right now the only documentation is "desktop-file-install --help".
desktop-file-validate takes a single argument, the file to validate. 

%prep
%setup -q
%patch0 -p0
%build
%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
cat > %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el << EOF
(autoload 'desktop-entry-mode "desktop-entry-mode" "Desktop Entry mode" t)
(add-to-list 'auto-mode-alist
'("\\\\.desktop\\\\(\\\\.in\\\\)?$" . desktop-entry-mode))
(add-hook 'desktop-entry-mode-hook 'font-lock-mode)
EOF

# automatic cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database.filter << EOF
^./usr/share/applications/.*\.desktop$
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database.script << EOF
#!/bin/sh
/usr/bin/update-desktop-database /usr/share/applications > /dev/null
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database.script

install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database-kde3.filter << EOF
^./opt/kde3/share/applications/.*\.desktop$
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database-kde3.script << EOF
#!/bin/sh
/usr/bin/update-desktop-database /opt/kde3/share/applications > /dev/null
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/update-desktop-database-kde3.script

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
%{_bindir}/*
%{_datadir}/emacs/site-lisp/desktop-entry-mode.el*
%{_var}/lib/rpm/filetriggers/update-desktop-database.*
%{_var}/lib/rpm/filetriggers/update-desktop-database-kde3.*
