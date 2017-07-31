# Co/Contra Variance

Generic types have special rules for type compatibility, referred to as covariance and contravariance. These rules determine whether _references of certain generic types are implicitly convertible to one another_ when _implicit conversions exist between their type arguments_. 

+ generic covariance, introduced in C# 4.0. 
+ delegate variance introduced in 3.0 

If a generic parameter is used only in _input positions_, it becomes **contravariant** (in), and when it only occurs in _output positions_, it becomes **covariant** (out). 

For this reason, the language requires you to be explicit about the intended variance annotation. _If no variance modifier is present, the type parameter will be treated as invariant_ (just as it was before C# 4.0).

## Delegates Return Type Variance 

**The return type of a method can derive from the type defined by the delegate**.

    public class DelegateReturnBase { }
    public class DelegateReturn : DelegateReturnBase { }

    public delegate DelegateReturnBase DelegateReturnBase_VoidParam_Delegate();


    public class DelegateParamBase { }
    public class DelegateParam : DelegateParamBase { }

    public delegate void VoidReturn_DelegateParam_Delegate(DelegateParam p);

    class Test
    {
        static DelegateReturn DelegateReturn_VoidParam_Method() {
            Console.WriteLine("call: DelegateReturn_VoidParam_Method");
            return new DelegateReturn();
        }

        static void VoidReturn_DelegateParamBase_Method(DelegateParamBase p) {
            Console.WriteLine("call: VoidReturn_DelegateParamBase_Method with param: {0}", p.GetType().Name);
        }

        public static void Go()
        {
            Console.WriteLine("DELEGATES RETURN TYPE VARIANCE");
            DelegateReturnBase_VoidParam_Delegate returnTypeVarianceDelegateInstance = DelegateReturn_VoidParam_Method;
            returnTypeVarianceDelegateInstance();
            Console.WriteLine("of type: {0}", returnTypeVarianceDelegateInstance.GetType().Name);

            Console.WriteLine("DELEGATES PARAMETER TYPE CONTRA-VARIANCE");
            VoidReturn_DelegateParam_Delegate paramContraVarDel = VoidReturn_DelegateParamBase_Method;
            paramContraVarDel(new DelegateParam());
            Console.WriteLine("of type: {0}", paramContraVarDel.GetType().Name);

        }
    }

## Delegates Parameter Type Contra-Variance 

The term parameter type contra-variance means that the parameters defined by the delegate might differ in the method that is called by the delegate. Here it’s different from the return type because the method might use a parameter type that derives from the type defined by the delegate. In the code sample the delegate uses the parameter type `DelegateParam2`, and the method that is assigned to the delegate instance d2 uses the parameter type `DelegateParam` that is the base type of DelegateParam2. 

daca tipul parametrului revine la baza in definitia delegatului => polimorfism. 

daca permut tipurile parametrilor => compile error delegate definition

    public event KeyPressEventHandler KeyPress;
    delegate void KeyPressEventHandler(object sender, KeyPressEventArgs e);
    txtAmount.KeyPress += this.LoggingHandler;
    void LoggingHandler(object sender, EventArgs e) {}

## Array Covariance

The array co-variance rules permit a value of an array type A[] to be a reference to an instance of an array type B[], _provided an implicit reference conversion exists from B to A_. Because of these rules, when an array element of a reference-type is passed as a reference or output parameter, a **run-time check is required to ensure that the actual element type of the array is identical to that of the parameter**.
The second invocation of F causes an ArrayTypeMismatchException to be thrown because the actual element type of b is string and not object. Array covariance specifically does not extend to arrays of value-types. For example, no conversion exists that permits an int[] to be treated as an object[].

            // defines
            static void F(ref object x) {}
            static void G(ref DelegateParamBase x) { }

            // tests
            object[] a = new object[10];
            object[] b = new string[10];

            F(ref a[0]); // Ok 
            try { F(ref b[1]); } catch (ArrayTypeMismatchException ex) { Console.WriteLine(ex.Message); }

            DelegateParamBase[] baseArray = new DelegateParamBase[10];
            DelegateParamBase[] specializedArray = new DelegateParam[10];

            G(ref baseArray[7]); // Ok 
            try { G(ref specializedArray[9]); }
            catch (ArrayTypeMismatchException ex) { Console.WriteLine(ex.Message); }
			
			
			
[<<](../csdotnet.md) 
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 

