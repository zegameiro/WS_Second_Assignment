import { motion } from "motion/react";
 
function Button({children,func}) {

  return (
    <motion.button className="bg-[#e10600] min-w-20 min-h-8 border-amber-100 border-2"
      onClick={func}
      whileHover={{
        x: -1,
        y: -1,
        boxShadow: "7px 7px #000"
      }}
      whileTap={{
        x:2,
        y:2,
        boxShadow: "0px 0px #000"
      }}
    >
        {children}
    </motion.button>
  )
}

export default Button;