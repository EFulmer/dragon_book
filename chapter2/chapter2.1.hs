type Digit = Int

data AddSub = Add AddSub Digit | Sub AddSub Digit | Digit 

instance Show AddSub where 
    show expr = case expr of 
                    Add x d -> (show x) ++ "+" ++ (show d)
                    Sub x d -> (show x) ++ "-" ++ (show d)
                    otherwise -> show expr
