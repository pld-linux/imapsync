%include	/usr/lib/rpm/macros.perl
Summary:	Mailboxes synchronization tool
Summary(pl):	Narz�dzie do synchroniczacji skrzynek pocztowych
Name:		imapsync
Version:	1.133
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.linux-france.org/prj/imapsync/dist/%{name}-%{version}.tgz
# Source0-md5:	dea4a2844652fabe90ee2bfe52fab1e2
URL:		http://www.linux-france.org/prj/imapsync/
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.202
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

%description -l pl
imapsync to narz�dzie u�atwiaj�ce przyrostowe rekurencyjne transfery
IMAP z jednej skrzynki do drugiej. Jest przydatne do migracji skrzynek
pocztowych i zmniajsza ilo�� przesy�anych danych kopiuj�c tylko
wiadomo�ci nie obecne na obu serwerach. Flagi oznaczaj�ce wiadomo�ci
przeczytane, nieprzeczytane i usuni�te s� zachowywane, a proces mo�e
by� zatrzymany i wznowiony. Oryginalne wiadomo�ci opcjonalnie mog� by�
usuni�te po udanym przes�aniu.

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
