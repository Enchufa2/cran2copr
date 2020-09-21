%global packname  tidytext
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Text Mining using 'dplyr', 'ggplot2', and Other Tidy Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 0.1.1
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-janeaustenr 
BuildRequires:    R-methods 
Requires:         R-CRAN-purrr >= 0.1.1
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-generics 
Requires:         R-Matrix 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-janeaustenr 
Requires:         R-methods 

%description
Using tidy data principles can make many text mining tasks easier, more
effective, and consistent with tools already in wide use. Much of the
infrastructure needed for text mining with tidy data frames already exists
in packages like 'dplyr', 'broom', 'tidyr', and 'ggplot2'. In this
package, we provide functions and supporting data sets to allow conversion
of text to and from tidy formats, and to switch seamlessly between tidy
tools and existing text mining packages.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
