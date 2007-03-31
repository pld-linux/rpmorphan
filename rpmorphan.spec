# TODO:
# - gui doesn't work
Summary:	rpmorphan - list the orphaned rpm packages
Summary(fr.UTF-8):	rpmorphan liste les packages rpm orphelins
Summary(pl.UTF-8):	rpmorphan - wyświetlanie listy osieroconych pakietów
Name:		rpmorphan
Version:	0.8
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/rpmorphan/%{name}-%{version}.tar.gz
# Source0-md5:	0a810de4b1c3f559b5a7de31731ec8f1
URL:		http://rpmorphan.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpmorphan finds "orphaned" packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages. It intends to be clone of
deborphan debian tools for rpm packages.

It will try to help you to remove unused packages, for exemple:
- after a distribution upgrade,
- when you want to suppress packages after some tests.

%description -l fr.UTF-8
Le logiciel rpmorphan liste les packages rpm qui n'ont plus de
dépendances avec les autres paquets installés sur votre systčme. C'est
un clone du logiciel deborphan de debian pour les packages rpm.

Il peut vous aider pour supprimer les packages inutilisés, par
exemple:
- aprčs une montée de version systčme,
- lors de la suppression de logiciels aprčs des tests.

%description -l pl.UTF-8
rpmorphan znajduje "osierocone" pakiety w systemie. Określa które
pakiety nie są zależnościami innych pakietów i wyświetla ich listę. W
zamyśle ma to być klon deborphana dla pakietów rpm.

Pomaga on usuwać nie używane pakiety, np.:
- po uaktualnieniu dystrybucji,
- kiedy chcemy usunąć pakiety po jakichś testach.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/var/lib/%{name}}

ln -sf rpmorphan.pl $RPM_BUILD_ROOT%{_bindir}/rpmorphan
ln -sf rpmusage.pl $RPM_BUILD_ROOT%{_bindir}/rpmusage

install {rpmorphan,rpmusage}.pl $RPM_BUILD_ROOT%{_bindir}
install {rpmorphan,rpmusage}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install keep $RPM_BUILD_ROOT/var/lib/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors Changelog NEWS Readme Todo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%dir /var/lib/%{name}
/var/lib/%{name}/keep
