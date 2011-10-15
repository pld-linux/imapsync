%include	/usr/lib/rpm/macros.perl
Summary:	Mailboxes synchronization tool
Summary(pl.UTF-8):	Narzędzie do synchroniczacji skrzynek pocztowych
Name:		imapsync
Version:	1.456
Release:	1
License:	WTFPL
Group:		Applications/Mail
#Source0:	http://www.linux-france.org/prj/imapsync/dist/%{name}-%{version}.tgz
Source0:	https://fedorahosted.org/released/imapsync/imapsync-1.456.tgz
# Source0-md5:	e9ea9ab5eba11cfe1c62ae9be1d9d7ae
URL:		http://www.linux-france.org/prj/imapsync/
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.202
Requires:	perl-Date-Manip
Requires:	perl-Mail-IMAPClient
Requires:	perl-Term-ReadKey
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
%setup -q

%build
%{__make}

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
