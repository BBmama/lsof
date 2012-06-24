Summary:	Lists files open by processes
Summary(es):	Lista los archivos abiertos por los procesos que est�n en ejecuci�n
Summary(pl):	Program do �ledzenia wszystkich proces�w w systemie
Summary(pt_BR):	Lista os arquivos abertos pelos processos que est�o rodando
Summary(ru):	���������� �������� ���������� �����
Summary(uk):	�����դ צ����Ԧ ��������� �����
Name:		lsof
Version:	4.60
Release:	2
License:	Free
Group:		Applications/System
Vendor:		Vic Abell <abe@purdue.edu>
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lsof/%{name}_%{version}_W.tar.gz
Patch0:		%{name}-linux-ipv6mapped.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lsof's name stands for LiSt Open Files, and it does just that. It
lists information about files that are open by the processes running
on a UNIX system.

%description -l es
El nombre lsof significa LiSt Open Files, y lo que hace es: lista los
archivos abiertos. Hace una relaci�n, con informaci�n variada, sobre
los archivos abiertos por los procesos en ejecuci�n en un sistema
UNIX.

%description -l pl
Lsof (LiSt Open Files) �ledzi wszystkie procesy jakie s� w danej
chwili uruchomine w systemie. Program ten jest bardzo pomocnym
narz�dziem dla administratora systemu Unix.

%description -l pt_BR
O nome lsof significa LiSt Open Files, e faz isto: lista os arquivos
abertos. Ele lista v�rias informa��es sobre os arquivos abertos pelos
processos que est�o rodando em um sistema UNIX.

%description -l ru
Lsof - ��� ���������� �� LiSt Open Files. ������ ��� ��������� lsof �
������ - ������� ���������� � ������, �������� ����������, �����������
� �������.

%description -l uk
Lsof - �� ���������� צ� LiSt Open Files. ���� �� �������� lsof �
������ - �������� �������æ� ��� �����, צ����Ԧ ���������� ���������.

%prep
%setup -c -q -n %{name}
tar xf %{name}_%{version}.tar
#%patch -p1

%build
cd %{name}_%{version}

./Configure -n linux
%{__make} \
	LSOF_CC="%{__cc}" \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd %{name}_%{version}

install lsof $RPM_BUILD_ROOT%{_sbindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf 00*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/00*

%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*
