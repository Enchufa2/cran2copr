%global packname  customLayout
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Arrange Elements on the R's Drawing Area or Inside thePowerPoint's Slide

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rvg 
Requires:         R-CRAN-gridExtra 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rvg 

%description
Create complicated drawing areas for multiple elements by combining much
simpler layouts. It is an extended version of layout function from the
'graphics' package, but it also works with 'grid' graphics. It also
supports arranging elements inside 'PowerPoint' slides created using the
'officer' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pptx
%{rlibdir}/%{packname}/INDEX
