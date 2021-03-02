
set -Ceu

cd $(dirname $0)

diff -u ./expected.txt <(j2cli5 ./template.j2 data1.yml data2.yml)
diff -u ./expected.txt <(cat ./template.j2 | j2cli5 - data1.yml data2.yml)


