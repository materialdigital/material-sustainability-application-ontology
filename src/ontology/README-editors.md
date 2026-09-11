These notes are for the EDITORS of matsus

This project was created using the [ontology development kit](https://github.com/INCATools/ontology-development-kit). See the site for details.

For more details on ontology management, please see the 
[OBO Academy Tutorials](https://oboacademy.github.io/obook/), the
[OBO tutorial](https://github.com/jamesaoverton/obo-tutorial) or the [Gene Ontology Editors Tutorial](https://go-protege-tutorial.readthedocs.io/en/latest/)

This documentation has been superceded by the ODK automatic documentation, which you can
activate by adding:

```
documentation:
  documentation_system: mkdocs
```

to your Makefile and running:

```
sh run.sh make update_repo
```
(Unix)

```
run.bat make update_repo
```
(Windows)

## Optional shared OAK cache

Set ODK_SHARE_OAK_CACHE to user, repo, or an explicit host directory before
invoking run.sh. The wrapper mounts that directory at the
repository-independent container location /work/.odk-cache/oaklib and sets
PYSTOW_HOME=/work/.odk-cache; it does not depend on a particular container
username or home directory.
