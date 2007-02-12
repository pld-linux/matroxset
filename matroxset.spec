Summary:	Utility to switch modes of matroxfb framebuffer devices
Summary(pl.UTF-8):   Narzędzie do zmiany trybów urządzeń framebuffera matroxfb
Name:		matroxset
Version:	0.4
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://platan.vc.cvut.cz/pub/linux/matrox-latest/%{name}-%{version}.tar.gz
# Source0-md5:	8f02b48c814c9f77bb7114f61420a2c3
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to switch modes of matroxfb framebuffer devices (switch heads,
activate TV-Out...).

%description -l pl.UTF-8
Narzędzie do zmiany trybów urządzeń framebuffera matroxfb
(przełączania głowic, włączania TV-Out...).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -W -Wall -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install matroxset $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc normal swapit swapped
%attr(755,root,root) %{_bindir}/*
