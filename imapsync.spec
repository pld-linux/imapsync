%include        /usr/lib/rpm/macros.perl
Summary:	Mailboxes synchronization tool
Name:		imapsync
Version:	1.133
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.linux-france.org/prj/imapsync/dist/%{name}-%{version}.tgz
# Source0-md5:	4b2f2cdd2a04e7e0ef65c9ca15f4481f
URL:		http://www.linux-france.org/prj/imapsync/
BuildRequires:	rpmbuild(macros) >= 1.202
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-base
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Term-ReadKey
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
