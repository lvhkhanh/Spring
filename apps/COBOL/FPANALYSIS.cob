       IDENTIFICATION DIVISION.
       PROGRAM-ID. FPANALYSIS.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-I        PIC 9(4) VALUE 0.
       01  WS-R        PIC 9(4) VALUE 0.
       01  WS-F        PIC 9(4) VALUE 0.
       01  WS-X        PIC 9(4) VALUE 0.
       01  WS-Q        PIC 9(4) VALUE 0.
       01  WS-FC       PIC 9(5) VALUE 0.
       01  WS-RESPONSE PIC X(80) VALUE SPACES.
       PROCEDURE DIVISION.
           DISPLAY "COBOL Function Point Analysis (AS/400/CL/RPG/DB2)"
           DISPLAY "Enter number of transaction inputs (I): " WITH NO ADVANCING
           ACCEPT WS-I

           DISPLAY "Enter number of reports (R): " WITH NO ADVANCING
           ACCEPT WS-R

           DISPLAY "Enter number of application-specific files (F): " WITH NO ADVANCING
           ACCEPT WS-F

           DISPLAY "Enter number of externally used files (X): " WITH NO ADVANCING
           ACCEPT WS-X

           DISPLAY "Enter number of query types (Q): " WITH NO ADVANCING
           ACCEPT WS-Q

           COMPUTE WS-FC = 4 * WS-I + 5 * WS-R + 10 * WS-F + 7 * WS-X + 4 * WS-Q
           DISPLAY "\nFunction Count (FC) = " WS-FC

           DISPLAY "\nExample: CRUD app best judgement" WITH NO ADVANCING
           DISPLAY "(I=4, R=2, F=1, X=1, Q=2 -> FC=51)"

           STOP RUN.
