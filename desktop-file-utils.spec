%global optflags %{optflags} --rtlib=compiler-rt

Summary:	Utilities for working with desktop entries
Name:		desktop-file-utils
Version:	0.26
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://freedesktop.org/Software/desktop-file-utils
Source0:	http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
BuildRequires:	emacs-bin
BuildRequires:	glibc-static-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(popt)

%description
desktop-file-utils contains a couple of command line utilities for working
with desktop entries. It requires GLib and popt to compile, because the
implementation requires Unicode utilities and such.

Right now the only documentation is "desktop-file-install --help".
desktop-file-validate takes a single argument, the file to validate. 

%prep
%autosetup -p1

%build
%configure

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
cat > %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el << EOF
(autoload 'desktop-entry-mode "desktop-entry-mode" "Desktop Entry mode" t)
(add-to-list 'auto-mode-alist
'("\\\\.desktop\\\\(\\\\.in\\\\)?$" . desktop-entry-mode))
(add-hook 'desktop-entry-mode-hook 'font-lock-mode)
EOF

# automatic cache update on rpm installs/removals
%transfiletriggerin -- %{_datadir}/applications/
%{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null 2> /dev/null

%files
%doc AUTHORS NEWS README ChangeLog
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/desktop-entry-mode.el*
