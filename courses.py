course_data = {
    # ---------------- AMC & CS----------------
    "AMA1113": {
        "title": "Differential Equations",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide knowledge in solutions of differential equations and its basic applications.",
        "lecturer": "Mr. Kuhaneshan",
        "resources": [
            {"name": "Differential Equations by Boyce & DiPrima", "link": "https://example.com/diff_eq"},
        ]
    },
    "PMA1113": {
        "title": "Foundation of Mathematics",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide a strong foundation in Mathematics to follow the remaining courses in Applied Mathematics and Computing."
    },
    "STA1113": {
        "title": "Introduction to Statistics",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide knowledge in how to summarize, interpret and present statistical information, probability reasoning and probability theory."
    },
    "CSC1113": {
        "title": "Foundation of Computer Science",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide the basic concepts in computer science and introduce basic software."
    },
    "CSC1123": {
        "title": "Introduction to Programming",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To introduce the principles of programming and to provide knowledge in structured programming concepts and techniques."
    },
    "AMA1213": {
        "title": "Methods of Applied Mathematics",
        "credits": 3,
        "prerequisites": "AMA1113",
        "objective": "To provide a broad understanding of Fourier approximation in various mathematical methods in physical system modelling."
    },
    "PMA1213": {
        "title": "Analysis and Number Theory",
        "credits": 3,
        "prerequisites": "PMA1113",
        "objective": "To provide a broad understanding of analysis techniques that are basic steppingstones for contemporary research."
    },
    "STA1213": {
        "title": "Statistical Inference",
        "credits": 3,
        "prerequisites": "STA1113",
        "objective": "To provide the basic elements of estimation of population parameters, various methods of hypothesis testing, and decision-making abilities."
    },
    "CSC1213": {
        "title": "Object Oriented Programming",
        "credits": 3,
        "prerequisites": "CSC1123",
        "objective": "To provide experience and confidence in the use of an object oriented programming using Java for problem solving activities."
    },
    "CSC1223": {
        "title": "Database Systems",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To enable students to design and develop an effective database for realistic applications and write complex database queries."
    },
    "AMA2113": {
        "title": "Optimization I",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To introduce the fundamental concepts of optimization techniques."
    },
    "AMA2122": {
        "title": "Vector Calculus",
        "credits": 2,
        "prerequisites": "AMA1113",
        "objective": "To introduce the methods of vector calculus and give the ability to use them for geometry and some physical concepts."
    },
    "PMA2113": {
        "title": "Linear Algebra",
        "credits": 3,
        "prerequisites": "PMA1113",
        "objective": "To provide knowledge in vectors, properties of matrices and its application to follow the other relevant courses."
    },
    "STA2113": {
        "title": "Design of Experiments",
        "credits": 3,
        "prerequisites": "STA1113, STA1213",
        "objective": "To provide basic elements of design of statistical experiments and analysis of variance methods."
    },
    "CSC2113": {
        "title": "Data Structures and Algorithms",
        "credits": 3,
        "prerequisites": "CSC1123, CSC1213",
        "objective": "To provide a solid background in essential components of data structures and algorithms."
    },
    "CSC2122": {
        "title": "Computer Security",
        "credits": 2,
        "prerequisites": "CSC1113",
        "objective": "To provide fundamental issues of computer security and network security."
    },
    "AMA2213": {
        "title": "Mechanics",
        "credits": 3,
        "prerequisites": "AMA1113, AMA2122",
        "objective": "To provide the mathematical concepts in dynamic and static systems."
    },
    "STA2213": {
        "title": "Sampling Theory",
        "credits": 3,
        "prerequisites": "STA1113, STA1213",
        "objective": "To provide the basic concepts and techniques in sampling methods and common errors that occur during the sampling process."
    },
    "CSC2212": {
        "title": "Data Communication and Computer Networks",
        "credits": 2,
        "prerequisites": "CSC1113",
        "objective": "To provide the basic concepts in data communication and computer network."
    },
    "CSC2222": {
        "title": "Software Engineering",
        "credits": 2,
        "prerequisites": "CSC1113",
        "objective": "To provide fundamental knowledge and skills to analyze and evaluate system demands and develop skills that will enable students to construct software of high quality."
    },
    "CSC2234": {
        "title": "Numerical Computing",
        "credits": 4,
        "prerequisites": "None",
        "objective": "To provide the basic concepts and techniques of numerical computing."
    },
    "AMA3113": {
        "title": "Mathematical Modelling",
        "credits": 3,
        "prerequisites": "AMA1113, AMA1213",
        "objective": "To provide mathematical modeling techniques using graphical, numerical, symbolic, and verbal techniques to describe and explore real-world data and phenomena."
    },
    "AMA3122": {
        "title": "Optimization II",
        "credits": 2,
        "prerequisites": "AMA2113",
        "objective": "To provide the advanced knowledge to develop linear optimization theory that apply for dynamic programming, goal programming, and game theory."
    },
    "STA3113": {
        "title": "Regression Analysis and Time Series",
        "credits": 3,
        "prerequisites": "STA1113, STA1213",
        "objective": "To provide knowledge in the simple and multiple regression analysis, how to use and interpret these results in a real world setting and the basic time series models."
    },
    "CSC3112": {
        "title": "Computer Graphics",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide background knowledge in the computer graphics concepts, methods and algorithms."
    },
    "CSC3123": {
        "title": "Operating Systems",
        "credits": 3,
        "prerequisites": "CSC1113, CSC1123, CSC2113",
        "objective": "To provide conceptual knowledge on structure and functions of modern operating systems."
    },
    "CSC3132": {
        "title": "Web Application Development",
        "credits": 2,
        "prerequisites": "CSC2212, CSC2222, CSC1213",
        "objective": "To provide concepts, methods and tools needed to develop basic web sites and client side and server side web applications."
    },
    "AMA3213": {
        "title": "Analytical Dynamics",
        "credits": 3,
        "prerequisites": "AMA1113, AMA1213, AMA2122, AMA2213",
        "objective": "To provide advanced theoretical developments, which solve dynamical problems and develop a deep understanding of the fundamentals of analytical dynamics."
    },
    "PMA3213": {
        "title": "Complex Variables",
        "credits": 3,
        "prerequisites": "PMA1113, PMA1213",
        "objective": "To provide an introduction to the theories for functions of a complex variable."
    },
    "STA3212": {
        "title": "Statistical Quality Control",
        "credits": 2,
        "prerequisites": "STA1113, STA1213, STA2213",
        "objective": "To provide the theory and methods of quality control including process capability, control charts, acceptance sampling, and process improvement."
    },
    "CSC3213": {
        "title": "Computer Architecture",
        "credits": 3,
        "prerequisites": "CSC1113, PMA1113, CSC1123, CSC2113",
        "objective": "To provide the concepts of modern computer system architecture and enable students to apply these insights and principles to future computer designs."
    },
    "CSC3222": {
        "title": "Graph Theory",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide a broad understanding of graph theory and its application in various fields of mathematics and computer science."
    },
    "CSC3232": {
        "title": "Group Project",
        "credits": 2,
        "prerequisites": "CSC1223, CSC2222, CSC3132",
        "objective": "To provide opportunity to synthesize knowledge from various areas of learning, and creatively apply it to real world problems."
    },
    "CSH3143": {
        "title": "Knowledge Representation and Programming in Logic",
        "credits": 3,
        "prerequisites": "PMA1113",
        "objective": "To provide knowledge in various techniques of knowledge representation and reasoning and to introduce programming in the PROLOG language."
    },
    "CSH3153": {
        "title": "Human Computer Interaction",
        "credits": 3,
        "prerequisites": "CSC1113",
        "objective": "To provide knowledge to design and construct user-friendly user interfaces."
    },
    "CSH3163": {
        "title": "Advanced Database System",
        "credits": 3,
        "prerequisites": "CSC1223",
        "objective": "To provide knowledge on advanced physical database system design principles, distributed databases, and emerging technologies."
    },
    "CSH3242": {
        "title": "Theory of Computation",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide the basic concepts in theoretical computer science, and the formal relationships among machines, languages and grammars."
    },
    "CSH3254": {
        "title": "Parallel Computing",
        "credits": 4,
        "prerequisites": "CSC1113, CSC1123",
        "objective": "To provide knowledge on characteristics of parallel architecture and parallelism of the standard algorithms."
    },
    "CSH3263": {
        "title": "Advanced Computer Networks",
        "credits": 3,
        "prerequisites": "CSC2212",
        "objective": "To provide knowledge in essential technologies and underlying theories of advanced computer networks."
    },
    "CSH3273": {
        "title": "Artificial Intelligence",
        "credits": 3,
        "prerequisites": "CSH3143",
        "objective": "To provide sound knowledge in artificial intelligence concepts and techniques."
    },
    "CSH4112": {
        "title": "System Analysis and Design",
        "credits": 2,
        "prerequisites": "CSC2222",
        "objective": "To provide fundamental concepts and trends of Systems Analysis and Design methods and practical techniques to analyze and design an information system.",
        "lecturer": "Dr. S. Kirushanth",
        "resources": [
            {"name": "J.L.Whitten and L.D.Bentley, Systems Analysis and Design Methods, 7th edition,Tata McGraw-Hill, 2007", "link": "https://example.com/diff_eq"},
            {"name": "K.E. Kendall and J.E. Kendall, Systems Analysis and Design, 9th edition, 2013", "link": "https://example.com/diff_eq"},
        ]
    },
    "CSH4123": {
        "title": "Bioinformatics",
        "credits": 3,
        "prerequisites": "STA1113, STA1213",
        "objective": "To provide brief knowledge on algorithms used in Bioinformatics and System Biology, the computational techniques in biology.",
        "lecturer": "Dr. T. Kartheeswaran",
        "resources": [
            {"name": "J.xiong, Essential Bioinformatics, Cambridge University Press, 1st edition, 2006", "link": "https://www.example.com"},
            {"name": "P. Compeau and P.A. Pevzner, Bioinformatics algorithms: an active learning approach, 2nd edition, 2015", "link": "https://www.example.com"},
        ]
    },
    "CSH4133": {
        "title": "Digital Image Processing",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide the principles, models and applications of Image processing and computer vision.",
        "lecturer": "Ms. S. Subaramya",
        "resources": [
            {"name": "R.C. Gonzalez and R.E.Woods, Digital Image Processing, Pearson, 4th edition, 2017", "link": "https://www.example.com"},
            {"name": "W. Burger and M.J. Burge, Principles of Digital Image Processing: Fundamental Techniques, Springer, 2009", "link": "https://www.example.com"},
        ]
    },
    "CSH4144": {
        "title": "Machine Learning",
        "credits": 4,
        "prerequisites": "STA1113, CSH3273",
        "objective": "To provide a complete introduction to machine learning, supervised, un supervised and semi-supervised issues and algorithms.",
        "lecturer": "Ms. R. Yasotha",
        "resources": [
            {"name": "C.M. Bishop, Pattern recognition and machine learning, Springer, 2011", "link": "https://www.example.com"},
            {"name": "D. Barber, Bayesian Reasoning and Machine Learning, 2012.", "link": "https://www.example.com"},
        ]
    },
    "CSH4152": {
        "title": "Cryptography",
        "credits": 2,
        "prerequisites": "CSC1123, PMA1213, CSC2122",
        "objective": "To provide concepts and various techniques of cryptography and its applications.",
        "lecturer": "Dr. R. Nagulan",
        "resources": [
            {"name": "J. Katz and Y. Lindell, Introduction to Modern Cryptography, 2nd edition, 2008.", "link": "https://www.example.com"},
            {"name": " C.P. Pfleeger, S.L. Pfleeger and J. Margulies, Security in Computing, Prentice-Hall, 5th edition, 2015.", "link": "https://www.example.com"},
        ]
    },
    "CSH4162": {
        "title": "Compiler Design",
        "credits": 2,
        "prerequisites": "CSH3242",
        "objective": "To provide the major concept areas of language translation and compiler design.",
        "lecturer": "Mr. S. Thirukumaran",
        "resources": [
            {"name": "R.K. Maurya, Compiler Design, 2011.", "link": "https://www.example.com"},
            {"name": "D. Grune and K.V. Reeuwijk, Modern Compiler Design, Springer, 2nd edition, 2012.", "link": "https://www.example.com"},
        ]
    },
    "CSH4173": {
        "title": "Numerical Linear Algebra and Finite Element Method",
        "credits": 3,
        "prerequisites": "AMA1113, PMA2113, CSC2234",
        "objective": "To provide knowledge in numerical methods for solving large systems of linear equations and theoretical background and applications of the Finite Element Method.",
         "lecturer": "Mr. S. Thilaganathan",
        "resources": [
            {"name": " Gene H. Golub and Charles F. Van Loan, Matrix Computations Johns Hopkins University Press, Baltimore, MD, USA, fourth edition, 2012.", "link": "https://www.amazon.com/Bioinformatics-Sequence-Genome-Analysis-Mount/dp/0879697121"},
            {"name": "William Ford, Numerical Linear Algebra with Applications: Using MATLAB, Academic Press, 2014.", "link": "https://www.example.com"},
        ]
    },
    "CSH4216": {
        "title": "Research Project",
        "credits": 6,
        "prerequisites": "-",
        "objective": "To develop skills on designing, implementing and reporting of scientific investigations."
    },
    "CSH4226": {
        "title": "Industrial Training",
        "credits": 6,
        "prerequisites": "-",
        "objective": "To provide opportunities for students to apply the computing knowledge, develop and consolidate practical computing skills."
    },

    # ---------------- ENVIRONMENTAL SCIENCE Level 1----------------
    "ENS1112": {
        "title": "Fundamentals in Environmental Chemistry",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide basic knowledge on environmental chemistry to understand the role of chemistry in environment."
    },
    "ENS1121": {
        "title": "Analysis of Chemical Elements and Compounds",
        "credits": 1,
        "prerequisites": "None",
        "objective": "To develop the basic laboratory skills in qualitative analysis of chemical elements and compounds."
    },
    "ENS1132": {
        "title": "Cell and Molecular Biology",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Understand the basics of cell and molecular biology and acquire knowledge for the future perception within the contexts of environmental science."
    },
    "ENS1142": {
        "title": "Plant Biology",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide conceptual knowledge on the identification and classification of plants on the aspect of plant diversity."
    },
    "ENS1153": {
        "title": "Fundamentals of Animal Biology",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Understand the importance of animal biology in term of diversity, evolution and environmental adaptations."
    },
    "ENS1162": {
        "title": "Basic Mathematics",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide the students with the basic knowledge on advanced mathematical operations."
    },
    "ENS1212": {
        "title": "Environment and Agriculture",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To enable the students to understand the impact of agriculture and its effect on the environment and vice versa."
    },
    "ENS1223": {
        "title": "Soil Science",
        "credits": 3,
        "prerequisites": "None",
        "objective": "To provide the knowledge on principles of environmental soil science and to develop the skills adopting the practices in effective soil fertility management."
    },
    "ENS1232": {
        "title": "Environmental Sanitation",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide knowledge to understand the sanitary issues in environment, different health and legal aspects of environmental sanitation."
    },
    "ENS1242": {
        "title": "Principles of Economics",
        "credits": 2,
        "prerequisites": "None",
        "objective": "To provide the basic conceptual knowledge on the microeconomics and macroeconomics."
    },

    # ---------------- INFORMATION TECHNOLOGY ----------------
    "IT1113": {
        "title": "Fundamentals of Information Technology",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide basic knowledge on IT components and apply computational tools to solve real-world problems.",
        "contents": "History of computing; computer organization; number systems; OS; DBMS; networking; Internet; emerging trends; application software.",
        "resources": [
            {"name": "Stair & Reynolds, \"Fundamentals of Information Systems\", 6th ed., 2012"},
            {"name": "Kanaganathan, \"Fundamentals of Information Technology\", 2006"},
            {"name": "Mathew & Murugeshan, \"Fundamentals of IT\", 2013"}
        ]
    },
    "IT1122": {
        "title": "Foundation of Mathematics",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Solve IT-related mathematical problems using appropriate techniques.",
        "contents": "Sets, relations, functions; propositional logic; Boolean algebra; Karnaugh maps; graphs/trees; automata.",
        "resources": [
            {"name": "Kolman & Busby, \"Discrete Mathematical Structures\", 2nd ed., 1987"},
            {"name": "Rosen, \"Discrete Mathematics\", 7th ed., 2012"},
            {"name": "Gersting, \"Mathematical Structures for CS\", 7th ed., 2014"}
        ]
    },
    "IT1134": {
        "title": "Fundamentals of Programming",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide knowledge on programming techniques and train to design, code, and debug programs.",
        "contents": "Algorithms, flowcharts; C++ basics; control structures; functions; recursion; arrays, pointers; exception handling.",
        "resources": [
            {"name": "Malik, \"C++ Programming\", 5th ed., 2011"},
            {"name": "Stroustrup, \"Programming: Principles and Practice Using C++\", 2nd ed., 2014"},
            {"name": "Deitel & Deitel, \"C++ How to Program\", 10th ed., 2016"}
        ]
    },
    "IT1144": {
        "title": "Fundamentals of Web Programming",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide knowledge on web-based programming to design interactive web pages.",
        "contents": "HTML structure; text formatting; links/images; forms/tables; CSS; multimedia embedding.",
        "resources": [
            {"name": "Duckett, \"Beginning HTML, XHTML, CSS, and JavaScript\", 2010"},
            {"name": "Deitel & Deitel, \"Internet & WWW How To Program\", 5th ed., 2011"},
            {"name": "Wempen, \"HTML5 Step by Step\", 2011"}
        ]
    },
    "IT1152": {
        "title": "Essentials of Statistics",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Understand the relationship between probability and statistics and their role in modeling practical problems.",
        "contents": "Descriptive stats; probability theory; random variables; binomial/normal distributions; hypothesis testing; applications in IT.",
        "resources": [
            {"name": "Baron, \"Probability and Statistics for CS\", 2nd ed., 2014"},
            {"name": "Montgomery & Runger, \"Applied Stats and Probability for Engineers\", 6th ed., 2014"},
            {"name": "Braun, \"Statistical Programming with R\", 2nd ed., 2016"}
        ]
    },
    "IT1214": {
        "title": "Object Oriented Design and Programming",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide knowledge on OOP concepts for application development.",
        "contents": "Classes/objects; inheritance; polymorphism; operator overloading; virtual functions; abstract classes.",
        "resources": [
            {"name": "Barnes, \"OOP with Java\", 2000"},
            {"name": "Wu, \"OOP with Java\", 5th ed., 2006"},
            {"name": "West et al., \"Head First OOAD\", 2011"}
        ]
    },
    "IT1223": {
        "title": "Database Management Systems",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on DB management and data retrieval for application development.",
        "contents": "DB systems; ER/EER modeling; relational model; SQL; normalization; data definition/manipulation.",
        "resources": [
            {"name": "Coronel et al., \"Database Systems\", 9th ed., 2011"},
            {"name": "Connolly & Begg, \"Database Systems\", 4th ed., 2005"},
            {"name": "Elmasri & Navathe, \"Fundamentals of DB Systems\", 7th ed., 2015"},
            {"name": "Ramakrishnan & Gehrke, \"DBMS\", 3rd ed., 2002"},
            {"name": "Sheldon & Moes, \"Beginning MySQL\", 2005"}
        ]
    },
    "IT1232": {
        "title": "Project Management",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide management and tech skills for successful IT project development.",
        "contents": "Project scope/time/cost/quality/risk management; work breakdown structure; stakeholder analysis; reporting.",
        "resources": [
            {"name": "Schwalbe, \"IT Project Management\", 7th ed., 2014"},
            {"name": "Marchewka, \"IT Project Management\", 5th ed., 2016"},
            {"name": "PMBOK Guide, 4th ed."}
        ]
    },
    "IT1242": {
        "title": "Principles of Computer Networks",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on data communication and computer networks.",
        "contents": "OSI/TCP/IP models; transmission media; multiplexing; switching; error detection/correction.",
        "resources": [
            {"name": "Tanenbaum & Wetherall, \"Computer Networks\", 5th ed., 2011"},
            {"name": "Kurose & Ross, \"Computer Networking\", 6th ed., 2013"},
            {"name": "Forouzan, \"Data Communications and Networking\", 4th ed., 2007"}
        ]
    },
    "IT1252": {
        "title": "Electronics and Device Interfacing",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on basic electronics and microcontroller programming.",
        "contents": "Semiconductors; diodes/transistors; op-amps; digital logic; microcontrollers; sensors; ADC/DAC; assembly/C programming.",
        "resources": [
            {"name": "Gaonkar, \"Microcontrollers\", 2007"},
            {"name": "Mazidi et al., \"AVR Microcontroller\", 2010"},
            {"name": "Rajendra, \"Fundamentals of Electronics\", 2008"}
        ]
    },
    "IT1262": {
        "title": "Mathematics for Computing",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide mathematical principles required for IT.",
        "contents": "Matrices; Gaussian elimination; limits/differentiation/integration; 2D/3D transforms; induction/recursion.",
        "resources": [
            {"name": "Davis, \"Linear Algebra and Probability for CS\", 2012"},
            {"name": "Prasad, \"Elementary Linear Algebra\", 2nd ed., 2012"},
            {"name": "Lay, \"Linear Algebra and Its Applications\", 4th ed., 2012"}
        ]
    },
    "IT2114": {
        "title": "Data Structures",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide methods of data representation for effective programming.",
        "contents": "Arrays, stacks, queues, linked lists; trees, graphs, hashing; sorting/searching; balanced trees, heaps.",
        "resources": [
            {"name": "Goodrich & Tamassia, \"Data Structures & Algorithms in Java\", 6th ed., 2014"},
            {"name": "Koffman & Wolfgang, \"Data Structures\", 3rd ed., 2015"},
            {"name": "Sahni, \"Data Structures in Java\", 2nd ed."}
        ]
    },
    "IT2122": {
        "title": "Software Engineering",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on software development processes.",
        "contents": "SDLC models; system modeling; architectural design; OOA (use cases, class modeling); testing; evolution.",
        "resources": [
            {"name": "Sommerville, \"Software Engineering\", 10th ed., 2015"},
            {"name": "Stephens, \"Beginning Software Engineering\", 2015"},
            {"name": "Pressman, \"SE: Practitioner's Approach\", 8th ed., 2014"}
        ]
    },
    "IT2133": {
        "title": "Advanced Web Programming",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on advanced web dev for dynamic applications.",
        "contents": "DNS/security; CMS; CSS advanced; JavaScript/jQuery/AJAX; PHP (forms, sessions, DB integration).",
        "resources": [
            {"name": "Zakas, \"Professional JavaScript\", 3rd ed., 2012"},
            {"name": "Nixon, \"Learning PHP, MySQL & JavaScript\", 4th ed., 2014"},
            {"name": "Duckett, \"JavaScript and JQuery\", 2014"}
        ]
    },
    "IT2143": {
        "title": "Visual Programming",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on visual components for user-friendly interfaces.",
        "contents": "GUI design; forms/controls/menus; event handling; DB connectivity; visual app development.",
        "resources": [
            {"name": "Troelsen, \"Pro C#\", 5th ed., 2010"},
            {"name": "Doyle, \"C# Programming\", 3rd ed., 2010"},
            {"name": "Hall, \"Adaptive Code via C#\", 2014"}
        ]
    },
    "IT2153": {
        "title": "Computer Graphics",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide algorithmic concepts to represent/manipulate 2D/3D objects.",
        "contents": "Graphics devices; line/circle algorithms; 2D/3D transforms; viewing; projection; clipping.",
        "resources": [
            {"name": "Hearn, \"Computer Graphics C version\", 2nd ed., 1996"},
            {"name": "Shirley & Marschner, \"Fundamentals of CG\", 3rd ed., 2009"},
            {"name": "Hearn, \"Computer Graphics with OpenGL\", 4th ed., 2010"},
            {"name": "Klawonn, \"Intro to CG using Java\", 2008"}
        ]
    },
    "IT2212": {
        "title": "Management Information Systems",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on IS architecture for organizational management.",
        "contents": "Types of IS; ERP/CRM/SCM; data warehousing; data mining; IT procurement; ethics/security.",
        "resources": [
            {"name": "Laudon et al., \"MIS – Managing the Digital Firm\", 14th ed., 2015"},
            {"name": "Rainer & Prince, \"MIS\", 3rd ed., 2015"},
            {"name": "Laudon & Laudon, \"MIS\", 2007"}
        ]
    },
    "IT2223": {
        "title": "Design and Analysis of Algorithms",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide fundamentals to design and analyze computational algorithms.",
        "contents": "Algorithm analysis; greedy/divide & conquer/backtracking/dynamic programming; graph/tree algorithms.",
        "resources": [
            {"name": "Baase & Van Gelder, \"Computer Algorithms\", 3rd ed., 2003"},
            {"name": "Cormen et al., \"Introduction to Algorithms\", 3rd ed., 2009"},
            {"name": "Levitin, \"Design and Analysis of Algorithms\", 3rd ed., 2011"}
        ]
    },
    "IT2234": {
        "title": "Web Services and Server Technologies",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide knowledge on web services and server administration.",
        "contents": "Client-server architecture; middleware; XML/DTD/XSLT; SOAP/WSDL; PHP socket programming; server management.",
        "resources": [
            {"name": "Konga, \"Basic Integrative Programming Technologies\", 2012"},
            {"name": "Anders & Schwartzbach, \"XML and Web Technologies\", 2006"},
            {"name": "Schlossnagle, \"Advanced PHP Programming\", 2004"}
        ]
    },
    "IT2244": {
        "title": "Operating Systems",
        "credits": 4,
        "prerequisites": "None",
        "objective": "Provide knowledge on OS structure and functions.",
        "contents": "Process/thread management; memory management; file systems; UNIX system programming; IPC.",
        "resources": [
            {"name": "Tanenbaum, \"Modern Operating Systems\", 4th ed., 2014"},
            {"name": "Stallings, \"OS: Internals and Design\", 8th ed., 2014"},
            {"name": "Bresnahan, \"Linux Command Line\", 3rd ed., 2015"}
        ]
    },
    "IT2252": {
        "title": "Social and Professional Issues in IT",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Explore ethics, privacy, and social issues in IT.",
        "contents": "Professional ethics; computer crime; privacy; IP (copyrights/patents); software piracy; teamwork.",
        "resources": [
            {"name": "Reynolds, \"Ethics in IT\", 5th ed., 2014"},
            {"name": "Brinkman, \"Ethics in a Computing Culture\", 2012"},
            {"name": "Kizza, \"Ethics in Computing\", 2016"}
        ]
    },
    "IT3113": {
        "title": "Knowledge Based Systems and Logic Programming",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on KB representation and logic programming.",
        "contents": "Predicate logic; expert systems; fuzzy logic; AI search (A*, BFS); classic problems; Prolog.",
        "resources": [
            {"name": "Akerkar & Sajja, \"Knowledge-Based Systems\", 2010"},
            {"name": "Russell & Norvig, \"AI: A Modern Approach\", 2011"},
            {"name": "Bramer, \"Logic Programming with Prolog\", 2nd ed., 2013"},
            {"name": "Clocksin & Mellish, \"Programming in Prolog\", 5th ed., 2013"},
            {"name": "Bratko, \"Prolog Programming for AI\", 3rd ed., 2001"}
        ]
    },
    "IT3122": {
        "title": "Computer Security",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on vulnerabilities and digital forensics in IT security.",
        "contents": "Symmetric/asymmetric crypto; hash/MAC/digital signatures; network/mobile/web security; firewalls; digital forensics.",
        "resources": [
            {"name": "Stallings, \"Cryptography and Network Security\", 5th ed., 2013"},
            {"name": "Kim & Solomon, \"Fundamentals of IS Security\", 2nd ed., 2013"},
            {"name": "Robinson, \"Digital Forensics Workbook\", 2015"},
            {"name": "Arnes, \"Digital Forensics\", 2017"}
        ]
    },
    "IT3133": {
        "title": "Mobile Communication and Computing",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on mobile voice/data architecture.",
        "contents": "GSM/3G/4G; MAC (FDMA/TDMA/CDMA); Mobile IP; TCP variants; MANETs; Bluetooth/WAP.",
        "resources": [
            {"name": "Gibson, \"Mobile Communications Handbook\", 3rd ed., 2012"},
            {"name": "Olenewa & Ciampa, \"Guide to Wireless Communications\", 3rd ed., 2013"},
            {"name": "Stallings, \"Wireless Communications & Networks\", 2nd ed., 2004"}
        ]
    },
    "IT3143": {
        "title": "Digital Image Processing",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide concepts and techniques for digital image processing.",
        "contents": "Image formation/sampling; color models; spatial/freq domain filtering; histogram processing; segmentation; compression.",
        "resources": [
            {"name": "Gonzalez & Woods, \"Digital Image Processing\", 3rd ed., 2016"},
            {"name": "Gonzalez & Woods, \"DIP using MATLAB\", 2nd ed., 2010"},
            {"name": "Soloman & Breckon, \"Fundamentals of DIP\", 2011"}
        ]
    },
    "IT3152": {
        "title": "Software Quality Assurance",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide approaches for software testing and QA.",
        "contents": "SQA process; test planning/design/execution; defect/incident management; quality metrics; testing tools.",
        "resources": [
            {"name": "Galin, \"Software Quality Assurance\", 2004"},
            {"name": "Godbole, \"Software Quality Assurance\", 2016"},
            {"name": "Laboon, \"A Friendly Intro to Software Testing\", 2016"},
            {"name": "Solis Tech, \"Quality Assurance Made Easy\", 2016"}
        ]
    },
    "IT3162": {
        "title": "Group Project",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide team-based software development experience.",
        "contents": "Team project (3–5 members); SDLC application; documentation; presentation; viva.",
        "resources": [
            {"name": "Barkley et al., \"Collaborative Learning Techniques\", 2005"},
            {"name": "Fincher et al., \"CS Project Work\", 2001"},
            {"name": "Layton, \"Agile Project Management For Dummies\", 2012"},
            {"name": "Dept. Guidelines"}
        ]
    },
    "IT3213": {
        "title": "Human Computer Interaction",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide design techniques for user-friendly interactive applications.",
        "contents": "HCI models; interaction design; usability evaluation; task/dialog design; emerging tech (VR/AR).",
        "resources": [
            {"name": "Dix et al., \"Human Computer Interaction\", 3rd ed., 2004"},
            {"name": "Preece et al., \"Interaction Design\", 4th ed., 2015"},
            {"name": "Solis Tech, \"HCI Fundamentals\", 2016"}
        ]
    },
    "IT3223": {
        "title": "Advanced Database Management Systems",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide advanced DB concepts for organizational use.",
        "contents": "EER/OO models; indexing/hashing; query optimization; transactions/concurrency; distributed DBs; data mining.",
        "resources": [
            {"name": "Silberschatz et al., \"Database System Concepts\", 6th ed., 2011"},
            {"name": "Elmasri & Navathe, \"Fundamentals of DB Systems\", 7th ed., 2015"},
            {"name": "Coronel et al., \"Database Systems\", 9th ed., 2011"}
        ]
    },
    "IT3232": {
        "title": "E-Commerce",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on e-technologies in e-commerce/business/banking/learning.",
        "contents": "E-business models; e-marketing; e-banking/payment; e-learning; legal/ethical issues; web app dev.",
        "resources": [
            {"name": "Laudon & Traver, \"E-Commerce 2015\", 11th ed., 2015"},
            {"name": "DevZone, \"Building eCommerce Applications\", 2011"},
            {"name": "Laudon & Traver, \"E-Commerce 2017\", 13th ed., 2017"}
        ]
    },
    "IT3243": {
        "title": "Parallel Computing",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on parallel architectures and algorithms.",
        "contents": "Flynn's taxonomy; decomposition; communication patterns; speedup/scalability; MPI programming.",
        "resources": [
            {"name": "Grama et al., \"Intro to Parallel Computing\", 2nd ed., 2003"},
            {"name": "Zinterhof et al., \"Parallel Computing: Numerics\", 2009"}
        ]
    },
    "IT3252": {
        "title": "Multimedia Computing",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on multimedia data representation and embedding.",
        "contents": "Data compression; media editors; VR/interactive media; multimedia systems; authoring; streaming.",
        "resources": [
            {"name": "Anitha, \"Computer Graphics and Multimedia Insights\", 2016"},
            {"name": "Vaughan, \"Multimedia: Making It Work\", 9th ed., 2014"},
            {"name": "Guzdial & Ericson, \"Intro to Computing with Java\", 2006"}
        ]
    },
    "IT3262": {
        "title": "Operations Research",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide techniques to solve real-life optimization problems.",
        "contents": "LP formulation/simplex; transportation/assignment models; PERT/CPM; sensitivity analysis.",
        "resources": [
            {"name": "Taha, \"Operations Research\", 9th ed., 2010"},
            {"name": "Gupta, \"Optimization Techniques\", 2012"},
            {"name": "Kunc & Malpass, \"Behavioral OR\", 2018"},
            {"name": "Panneerselvam, \"Operations Research\", 2nd ed., 2009"}
        ]
    },
    "IT4113": {
        "title": "Computer Organization and Architecture",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on computer performance and processing architecture.",
        "contents": "CPU/memory/I/O organization; pipelining; cache/memory hierarchy; assembly programming.",
        "resources": [
            {"name": "Hennessy & Patterson, \"Computer Architecture\", 6th ed., 2017"},
            {"name": "Stallings, \"Computer Organization and Architecture\", 8th ed., 2012"},
            {"name": "Brey, \"Intel Microprocessors\", 8th ed., 2008"},
            {"name": "Turbo Assembler User Guide, v5, 1995"},
            {"name": "Swan, \"Mastering Turbo Assembler\", 2nd ed., 1995"}
        ]
    },
    "IT4123": {
        "title": "Agent Based Computing",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide knowledge on agent-based system design.",
        "contents": "Agent types/BDI; mobile/multi-agent systems; KQML/FIPA; agent communication/toolkits.",
        "resources": [
            {"name": "Luck et al., \"Agent Technology\", 2003"},
            {"name": "Wooldridge, \"Intro to Multi-Agent Systems\", 2nd ed., 2002"},
            {"name": "Xu, \"Practical Applications of Agent-Based Technology\", 2012"}
        ]
    },
    "IT4133": {
        "title": "Bioinformatics and Computational Biology",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide computational algorithms for biological applications.",
        "contents": "Molecular biology basics; sequence alignment; phylogeny; proteomics; genomics; ML in bioinformatics.",
        "resources": [
            {"name": "Jones & Pevzner, \"Intro to Bioinformatics Algorithms\", 2004"},
            {"name": "Xiong, \"Essential Bioinformatics\", 2006"},
            {"name": "Ramsden, \"Bioinformatics\", 3rd ed., 2016"}
        ]
    },
    "IT4142": {
        "title": "Compiler Design",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide essential aspects of compilers and related tools.",
        "contents": "Lexical/syntax/semantic analysis; grammars; parsing (LL/LR); symbol tables; code generation/optimization.",
        "resources": [
            {"name": "Hunter, \"The Essence of Compilers\", 2004"},
            {"name": "Aho et al., \"Compilers: Principles, Techniques, and Tools\", 2nd ed., 2012"}
        ]
    },
    "IT4153": {
        "title": "Advanced Computer Networks",
        "credits": 3,
        "prerequisites": "None",
        "objective": "Provide advanced network functionalities, protocols, and techniques.",
        "contents": "Internetworking; routing protocols; Cisco IOS; VLANs; switching; wireless; network management.",
        "resources": [
            {"name": "Kurose & Ross, \"Computer Networking\", 6th ed., 2013"},
            {"name": "Peterson & Davie, \"Computer Networks\", 5th ed., 2011"},
            {"name": "Stallings, \"Data and Computer Communications\", 10th ed., 2014"}
        ]
    },
    "IT4216": {
        "title": "Research Project",
        "credits": 6,
        "prerequisites": "None",
        "objective": "Provide experience to critically analyze research and propose methodology.",
        "contents": "Individual research; proposal; monthly reports; thesis; presentation; viva.",
        "resources": [
            {"name": "Zobel, \"Writing for Computer Science\", 2007"},
            {"name": "Booth et al., \"The Craft of Research\", 2003"},
            {"name": "Nandi, \"Learning Research\", 2005"}
        ]
    },
    "IT4226": {
        "title": "Industrial Training",
        "credits": 6,
        "prerequisites": "None",
        "objective": "Provide hands-on experience in an IT industry.",
        "contents": "6-month industry placement; weekly diary; final report; presentation.",
        "resources": [
            {"name": "Industrial Training Guidelines and Diary, Dept. of Physical Science, Vavuniya Campus, 2018"}
        ]
    },
    "EL4112": {
        "title": "Augmented and Virtual Reality",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on VR/AR representation of real-world scenarios.",
        "contents": "VR/AR architecture/hardware; tracking/locomotion; haptics; applications (medicine, education); health issues; Unity/Unreal.",
        "resources": [
            {"name": "Ong & Nee, \"VR & AR in Manufacturing\", 2011"},
            {"name": "Ma & Grafe, \"VR & AR in Industry\", 2012"},
            {"name": "Ma et al., \"VR/AR for Healthcare\", 2014"}
        ]
    },
    "EL4122": {
        "title": "Data Science",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide Big Data analytics techniques using data mining.",
        "contents": "Data mining process/tools; data warehousing; Big Data fundamentals; analytics lifecycle; R.",
        "resources": [
            {"name": "Han et al., \"Data Mining\", 3rd ed., 2012"},
            {"name": "Witten et al., \"Data Mining\", 3rd ed., 2011"},
            {"name": "EMC, \"Data Science & Big Data Analytics\", 2015"},
            {"name": "Erl et al., \"Big Data Fundamentals\", 2016"}
        ]
    },
    "EL4132": {
        "title": "GIS and Remote Sensing",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide theoretical background of GIS and remote sensing.",
        "contents": "EMR interactions; satellite sensors (Landsat, SPOT); image classification; GIS data models; projections.",
        "resources": [
            {"name": "Campbell & Wynne, \"Intro to Remote Sensing\", 5th ed., 2011"},
            {"name": "Jensen, \"Introductory Digital Image Processing\", 3rd ed., 2004"},
            {"name": "Lillesand et al., \"Remote Sensing\", 7th ed., 2015"}
        ]
    },
    "EL4142": {
        "title": "Graph Theory",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide problem formulation/solving using graph theory.",
        "contents": "Graphs/trees; connectivity; Euler/Hamilton paths; planarity; network flows; coloring.",
        "resources": [
            {"name": "Chartrand & Zhang, \"First Course in Graph Theory\", 2012"},
            {"name": "Buckley & Lewinter, \"Introductory Graph Theory\", 2013"},
            {"name": "Deo, \"Graph Theory with Applications\", 2016"}
        ]
    },
    "EL4152": {
        "title": "Machine Learning",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide machine intelligence techniques for automated learning.",
        "contents": "Supervised/unsupervised/semi-supervised learning; classifiers (SVM, NN); clustering; NLP; fuzzy logic.",
        "resources": [
            {"name": "Bishop, \"Pattern Recognition & ML\", 2011"},
            {"name": "Barber, \"Bayesian Reasoning & ML\", 2012"}
        ]
    },
    "EL4162": {
        "title": "Numerical Computing",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide computational approaches for numerical problems.",
        "contents": "Root finding; interpolation; numerical diff/integration; linear systems (direct/iterative solvers).",
        "resources": [
            {"name": "Cheney & Kincaid, \"Numerical Mathematics\", 2012"},
            {"name": "Atkinson & Han, \"Elementary Numerical Analysis\", 3rd ed., 2003"},
            {"name": "Burden & Faires, \"Numerical Analysis\", 10th ed., 2015"},
            {"name": "Kanaganathan, \"Fundamentals of Numerical Computing\", 2009"}
        ]
    },
    "EL4172": {
        "title": "Optical Networks",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on optical switch architectures and trends.",
        "contents": "WDM; optical switching; routing/wavelength assignment; survivability; Li-Fi; data center networks.",
        "resources": [
            {"name": "Ramaswami et al., \"Optical Networks\", 3rd ed., 2010"},
            {"name": "Agrawal, \"Fiber-Optic Communication Systems\", 4th ed., 2010"},
            {"name": "Cvijetic & Djordjevic, \"Advanced Optical Communication Systems\", 2013"}
        ]
    },
    "EL4182": {
        "title": "Smart Systems",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide knowledge on designing automated systems using IoT.",
        "contents": "Sensors/actuators; signal processing; WSNs; smart home/medical systems; RFID/NFC; IoT gateways.",
        "resources": [
            {"name": "Holler et al., \"From M2M to IoT\", 2014"},
            {"name": "Al-Qutayri, \"Smart Home Systems\", 2010"},
            {"name": "Meijer et al., \"Smart Sensor Systems\", 2014"}
        ]
    },
    "EL4192": {
        "title": "Software Defined Networking",
        "credits": 2,
        "prerequisites": "None",
        "objective": "Provide concepts, architectures, and frameworks of SDN.",
        "contents": "Control/data plane separation; OpenFlow; SDN controllers; traffic engineering; data centers.",
        "resources": [
            {"name": "Nadeau & Gray, \"SDN: Software Defined Networks\", 2013"},
            {"name": "Azodolmolky, \"SDN with OpenFlow\", 2013"},
            {"name": "Goransson et al., \"Software Defined Networks\", 2nd ed., 2016"}
        ]
    }
}