# TODO:
# - consider move %{_bindir}/rpmorphan-lib.pl to other place
# - rpmduplicate show multilib packages as duplicated, IMO this is incorrect
#   # rpmduplicate
#   duplicate fam-libs : 2.7.0-7 (Fri Mar  2 01:55:12 2007) / 2.7.0-7 (Fri Mar  2 03:47:52 2007)
#   suggest : rpm -e fam-libs-2.7.0-7
#   # rpm -q fam-libs
#   fam-libs-2.7.0-7.x86_64
#   fam-libs-2.7.0-7.i686
# - rpmdeps doesn't support provides, it shows them as missing
#   "WARNING can not find who provide XXX" where XXX is not installed provide
%include	/usr/lib/rpm/macros.perl
Summary:	rpmorphan - list the orphaned rpm packages
Summary(fr.UTF-8):	rpmorphan liste les packages rpm orphelins
Summary(pl.UTF-8):	rpmorphan - wyświetlanie listy osieroconych pakietów
Name:		rpmorphan
Version:	1.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/rpmorphan/%{name}-%{version}.tar.gz
# Source0-md5:	8d4809df20807aa7ca3f8c51318e3df9
URL:		http://rpmorphan.sourceforge.net/
BuildRequires:	rpm-perlprov
Suggests:	perl-Curses-UI
Suggests:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpmorphan finds "orphaned" packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages. It intends to be clone of
deborphan debian tools for rpm packages.

It will try to help you to remove unused packages, for example:
- after a distribution upgrade,
- when you want to suppress packages after some tests.

Several tools are also provided:
- rpmusage - display rpm packages last use date
- rpmdep - display the full dependency of an installed rpm package
- rpmduplicates - find programs with several version installed

%description -l fr.UTF-8
Le logiciel rpmorphan liste les packages rpm qui n'ont plus de
dépendances avec les autres paquets installés sur votre systčme. C'est
un clone du logiciel deborphan de debian pour les packages rpm.

Il peut vous aider pour supprimer les packages inutilisés, par
exemple:
- aprčs une montée de version systčme,
- lors de la suppression de logiciels aprčs des tests.

Plusieurs outils sont également fournis:
- rpmusage - donne la date de la derničre utilisation d'un package
- rpmdep - founit l'ensemble des dependances (recursive) d'un package
- rpmduplicates - cherche les logiciels qui ont plusieurs versions
  installées

%description -l pl.UTF-8
rpmorphan znajduje "osierocone" pakiety w systemie. Określa które
pakiety nie są zależnościami innych pakietów i wyświetla ich listę. W
zamyśle ma to być klon deborphana dla pakietów rpm.

Pomaga on usuwać nie używane pakiety, np.:
- po uaktualnieniu dystrybucji,
- kiedy chcemy usunąć pakiety po jakichś testach.

Dostarcza dodatkowo narzędzia:
- rpmusage - wyświetla
- rpmdep - wyświetla pełne zależności zainstalowanego pakietu
- rpmduplicates - wyszukuje programy zainstalowane w kilku wersjach

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/var/lib/%{name},%{_sysconfdir},/var/log/}

install rpmdep.pl $RPM_BUILD_ROOT%{_bindir}/rpmdep
install rpmduplicates.pl $RPM_BUILD_ROOT%{_bindir}/rpmduplicates
install rpmorphan.pl $RPM_BUILD_ROOT%{_bindir}/rpmorphan
install rpmusage.pl $RPM_BUILD_ROOT%{_bindir}/rpmusage

install rpmorphan-lib.pl $RPM_BUILD_ROOT%{_bindir}

install {rpmdep,rpmduplicates,rpmorphan,rpmusage}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install rpmorphanrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/rpmorphanrc

install keep $RPM_BUILD_ROOT/var/lib/%{name}

touch $RPM_BUILD_ROOT/var/log/%{name}.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors Changelog NEWS Readme Todo
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rpmorphanrc
%{_mandir}/man1/rpmdep.1*
%{_mandir}/man1/rpmduplicates.1*
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%attr(640,root,root) %ghost /var/log/%{name}.log
%dir /var/lib/%{name}
/var/lib/%{name}/keep
