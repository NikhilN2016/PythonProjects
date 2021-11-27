print("Welcome to the console.")
print("The console is nothing but a history of your actions on this calculator")
ufo = codesters.Sprite("ufo", 0, 0)
ufo.set_size(0.4)
firstnumber = 0
secondnumber = 0
print("CMD: Float released")
choice = ufo.ask("Addition, Subtraction, Multiplication, Division, Exponent, Square root, Absolute value or type Advanced Math for more")
print("CMD: TypedChoice")
if choice == "Addition":
    Firstnumberaddition = float(ufo.ask("Enter first number"))
    print("CMD: AskedFirstAddent")
    firstnumber = Firstnumberaddition
    Secondnumberaddition = float(ufo.ask("Enter second number"))
    print("CMD: AskedSecondAddent")
    secondnumber = Secondnumberaddition
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(firstnumber + secondnumber)
    print("CMD: AddedNumbers")
if choice == "Subtraction":
    Firstnumbersubtraction = float(ufo.ask("Enter first number"))
    print("CMD: AskedMinuend")
    firstnumber = Firstnumbersubtraction
    Secondnumbersubtraction = float(ufo.ask("Enter second number"))
    print("CMD: AskedSubtrahend")
    secondnumber = Secondnumbersubtraction
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(firstnumber - secondnumber)
    print("CMD: SubtractedNumbers")
if choice == "Multiplication":
    Firstnumbermultiplication = float(ufo.ask("Enter first number"))
    print("CMD: AskedFirstFactor")
    firstnumber = Firstnumbermultiplication
    Secondnumbermultiplication = float(ufo.ask("Enter second number"))
    print("CMD: AskedSecondFactor")
    secondnumber = Secondnumbermultiplication
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(firstnumber * secondnumber)
    print("CMD: MultipliedNumbers")
if choice == "Division":
    Firstnumberdivision = float(ufo.ask("Enter first number"))
    print("CMD: AskedDivident")
    firstnumber = Firstnumberdivision
    Secondnumberdivision = float(ufo.ask("Enter second number"))
    print("CMD: AskedDivisor")
    secondnumber = Secondnumberdivision
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(firstnumber / secondnumber)
    print("CMD: DividedNumbers")
if choice == "Exponent":
    base = float(ufo.ask("Enter a number"))
    print("CMD: AskedBase")
    exponent = float(ufo.ask("Enter a exponent"))
    print("CMD: AskedExponent")
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(base ** exponent)
    print("CMD: FoundThePowerOf")
if choice == "Square root":
    sqrt = float(ufo.ask("Enter a number"))
    print("CMD: EnteredSQRTNumber")
    ans = math.sqrt(sqrt)
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(ans)
    print("CMD: FoundSQRTOf")
if choice == "Absolute value":
    absAsk = float(ufo.ask("Enter a number"))
    print("CMD: EnteredABSNumber")
    ans = abs(absAsk)
    ufo.say("The answer to that is...")
    stage.wait(2)
    ufo.say(ans)
    print("CMD: FoundABSOf")
if choice == "Advanced Math":
    print("CMD: LoadedAdvMath = Success")
    advanced_choice = ufo.ask("Pythagorus Theorem, Cos, Tan, Sin, Acos, Atan, Asin, Log base e, Log base")
    if advanced_choice == "Pythagorus Theorem":
        A = float(ufo.ask("Enter hypotenuse"))
        print("CMD: EnteredHypotenuse")
        B = float(ufo.ask("Enter adjacent"))
        print("CMD: EnteredAdj")
        answer = ((A ** 2) + (B ** 2))
        sqrt = math.sqrt(answer)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(sqrt)
        print("PythagorusTheorem")
    if advanced_choice == "Cosine":
        Numbercos = float(ufo.ask("Enter a number"))
        print("CMD: CosineNumber")
        cos = Numbercos
        rad_cos = math.radians(cos)
        answer = math.cos(rad_cos)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: Cosine")
    if advanced_choice == "Tangent":
        Numbertan = float(ufo.ask("Enter a number"))
        print("CMD: TangentNumber")
        tan = Numbertan
        rad_tan = math.radians(tan)
        answer = math.tan(rad_tan)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: Tangent")
    if advanced_choice == "Sine":
        NumberSin = float(ufo.ask("Enter a number"))
        print("CMD: SineNumber")
        sin = Numbersin
        rad_sin = math.radians(sin)
        answer = math.tan(rad_sin)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: Sine")
    if advanced_choice == "Acos":
        Numberacos = float(ufo.ask("Enter a number"))
        print("CMD: AcosNumber")
        aCos = Numberacos
        answer = math.acos(aCos)
        degree_answer = math.degrees(answer)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: Acos")
    if advanced_choice == "Atan":
        Numberatan = float(ufo.ask("Enter a number"))
        print("CMD: AtanNumber")
        aTan = Numberatan
        answer = math.atan(aTan)
        degree_answer = math.degrees(answer)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: Atan")
    if advanced_choice == "Asin":
        Numberasin = float(ufo.ask("Enter a number"))
        print("CMD: AsinNumber")
        aSin = Numberasin
        answer = math.asin(aSin)
        degree_answer = math.degrees(answer)
        ufo.say("The answer to that is...")
        stage.wait(2)
        print("CMD: Asin")
        ufo.say(answer)
    if advanced_choice == "Log base e":
        NumberLog = float(ufo.ask("Enter a number"))
        print("CMD: LogBaseENumber")
        Log = NumberLog
        answer = math.log(Log)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: LogBaseE")
    if advanced_choice == "Log base 10":
        NumberLog = float(ufo.ask("Enter a number"))
        print("CMD: LogBase10Number")
        Log = NumberLog
        answer = math.log(Log, 10)
        ufo.say("The answer to that is...")
        stage.wait(2)
        ufo.say(answer)
        print("CMD: LogBase10")



