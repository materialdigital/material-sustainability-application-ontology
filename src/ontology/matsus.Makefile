## Customize Makefile settings for matsus
##
## PMDco is the complete fixed backbone of Mat.Sus.
## Keep the complete pinned mirror instead of extracting an SLME module.

$(IMPORTDIR)/pmdco_import.owl: $(MIRRORDIR)/pmdco.owl | $(IMPORTDIR)
	cp $< $@

# Keep the primary serialization formats under one canonical ontology IRI.
# ODK's generated rules otherwise derive the ontology IRI from each filename.
MATSUS_CANONICAL_ONTOLOGY_IRI = $(ONTBASE)/
MATSUS_DEVELOPMENT_VERSION_IRI = $(ONTBASE)/dev/

$(ONT).owl: $(ONT)-full.owl
	$(ROBOT) annotate --input $< \
		--ontology-iri $(MATSUS_CANONICAL_ONTOLOGY_IRI) \
		--version-iri $(MATSUS_DEVELOPMENT_VERSION_IRI) \
		--annotation owl:versionInfo $(VERSION) \
		convert -o $@.tmp.owl && mv $@.tmp.owl $@

$(ONT).ttl: $(ONT).owl
	$(ROBOT) convert --input $< --check false --format ttl \
		--output $@.tmp.ttl && mv $@.tmp.ttl $@

$(ONT).json: $(ONT).owl
	$(ROBOT) convert --input $< --check false --format json \
		--output $@.tmp.json && mv $@.tmp.json $@

