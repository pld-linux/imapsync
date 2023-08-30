%bcond_with     tests
Summary:	Mailboxes synchronization tool
Summary(pl.UTF-8):	Narzędzie do synchroniczacji skrzynek pocztowych
Name:		imapsync
Version:	2.229
Release:	1
License:	NOLIMIT Public License
Group:		Applications/Mail
Source0:	https://github.com/imapsync/imapsync/archive/%{name}-%{version}.tar.gz
# Source0-md5:	efae792ba984469ec106573a0141f56c
Patch0:		no-prereq-install.patch
URL:		http://imapsync.lamiral.info/
BuildRequires:	cpanminus
BuildRequires:	perl-Authen-NTLM
BuildRequires:	perl-Crypt-OpenSSL-RSA
BuildRequires:	perl-Data-Uniqid
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Dist-CheckConflicts
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-IO-Socket-INET6
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-IO-Tee
BuildRequires:	perl-JSON-WebToken
BuildRequires:	perl-Mail-IMAPClient >= 3.29
BuildRequires:	perl-Module-ScanDeps
BuildRequires:	perl-Net-SSLeay
BuildRequires:	perl-PAR-Packer
BuildRequires:	perl-Package-Stash-XS
BuildRequires:	perl-Readonly
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Sys-MemInfo
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-MockObject
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-Unicode-String
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.202
%if %{with tests}
BuildRequires:  perl-Encode-IMAPUTF7
BuildRequires:  time
%endif
Requires:	perl-Authen-NTLM
Requires:	perl-Data-Uniqid
Requires:	perl-Date-Manip
Requires:	perl-Digest-HMAC
Requires:	perl-File-Copy-Recursive
Requires:	perl-HTML-Parser
Requires:	perl-IO-Tee
Requires:	perl-JSON
Requires:	perl-JSON-WebToken
Requires:	perl-Mail-IMAPClient >= 3.29
Requires:	perl-Term-ReadKey
Requires:	perl-Test-MockObject
Requires:	perl-URI
Requires:	perl-Unicode-String
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox
migration, and reduces the amount of data transferred by only copying
messages that are not present on both servers. Read, unread, and
deleted flags are preserved, and the process can be stopped and
resumed. The original messages can optionally be deleted after a
successful transfer.

%description -l pl.UTF-8
imapsync to narzędzie ułatwiające przyrostowe rekurencyjne transfery
IMAP z jednej skrzynki do drugiej. Jest przydatne do migracji skrzynek
pocztowych i zmniajsza ilość przesyłanych danych kopiując tylko
wiadomości nie obecne na obu serwerach. Flagi oznaczające wiadomości
przeczytane, nieprzeczytane i usunięte są zachowywane, a proces może
być zatrzymany i wznowiony. Oryginalne wiadomości opcjonalnie mogą być
usunięte po udanym przesłaniu.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

sed -E -i -e '1s,#!\s*/usr/bin/env\s+perl(\s|$),#!%{__perl}\1,' \
      imapsync

%build
%{__make}

%{?with_tests:%{__make} tests}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/imapsync
%{_mandir}/man1/imapsync.1*
