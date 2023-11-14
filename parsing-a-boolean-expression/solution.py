class Solution:
    def parseBoolExpr(self, x: str) -> bool:
      x=x.replace("t","True")
      x=x.replace("f","False")
      x=x.replace("!(","not any([")
      x=x.replace("&(","all([")
      x=x.replace("|(","any([")
      x=x.replace(")","])")
      return eval(x)