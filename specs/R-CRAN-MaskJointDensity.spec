%global packname  MaskJointDensity
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Masking, Unmasking and Restoring Confidential Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-np 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-MASS 

%description
Three key functionalities are present. It is able to mask confidential
data using multiplicative noise. It is able to unmask this data while
still preserving confidentiality. It is able to calculate the numerical
joint density function of the original data from the unmasked data, as
well as obtaining a sample from the marginal density functions of the
unmasked data. The final results are a reasonable approximation to the
original data for the purposes of analysis (Lin et al. (2018)
<http://www.tdp.cat/issues16/abs.a271a17.php>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
