def deduplicate(candidates, i=0):
  # load existing candidates into a dict
  span_dict = { unicode(cand.get_arguments()[i].parent) : list() for cand in candidates }
  for cand in candidates:
    span = cand.get_arguments()[i] # note: assumes this is not a relation
    span_dict[unicode(span.parent)].append( (span.char_start, span.char_end) )

  def nested(ivl1, ivl2):
    if ivl1 != ivl2 and ivl2[0] <= ivl1[0] <= ivl1[1] <= ivl2[1]:
        return True
    else:
        return False

  new_candidates = list()
  for cand in candidates:
      span = cand.get_arguments()[i]
      span_ivl = span.char_start, span.char_end
      span_name = unicode(span.parent)
      if all([not nested(span_ivl, other_ivl) for other_ivl in span_dict[span_name]]):
          yield cand

def filter_cand(candidates, filter_fn):
  for cand in candidates:
    if filter_fn(cand):
      yield cand