%define name	desktop-file-utils	
%define version 0.13
%define release %mkrel 1

Name:		%name
Summary:	Utilities for working with desktop entries
Version:	%version
Release:	%release
Source:		http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.bz2
# (fc) 0.11-5mdv encoding is deprecated
Patch2:		desktop-file-utils-0.11-encoding.patch

Url: 		http://freedesktop.org/Software/desktop-file-utils
Group:		Graphical desktop/Other
Buildrequires:	popt-devel glibc-static-devel 
BuildRequires:	glib2-devel
BuildRequires:	emacs-bin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPL

%description
desktop-file-utils contains a couple of command line utilities for working
with desktop entries. It requires GLib and popt to compile, because the
implementation requires Unicode utilities and such.

Right now the only documentation is "desktop-file-install --help".
desktop-file-validate takes a single argument, the file to validate. 

%prep
%setup -q
%patch2 -p1 -b .encoding

%build
%configure2_5x

%make

%install
rm -rf %buildroot

%makeinstall
mkdir -p %buildroot%_sysconfdir/emacs/site-start.d/
cat > %buildroot%_sysconfdir/emacs/site-start.d/%name.el << EOF
(autoload 'desktop-entry-mode "desktop-entry-mode" "Desktop Entry mode" t)
(add-to-list 'auto-mode-alist
'("\\\\.desktop\\\\(\\\\.in\\\\)?$" . desktop-entry-mode))
(add-hook 'desktop-entry-mode-hook 'font-lock-mode)
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/emacs/site-start.d/%name.el
%{_bindir}/*
%_datadir/emacs/site-lisp/desktop-entry-mode.el*
%doc AUTHORS NEWS README ChangeLog
