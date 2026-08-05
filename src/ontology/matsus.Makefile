## Customize Makefile settings for matsus
##
## PMDco is the complete fixed backbone of Mat.Sus.
## Keep the complete pinned mirror instead of extracting an SLME module.

$(IMPORTDIR)/pmdco_import.owl: $(MIRRORDIR)/pmdco.owl | $(IMPORTDIR)
	cp $< $@

