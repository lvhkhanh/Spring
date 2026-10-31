       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-EOF            PIC X VALUE 'N'.
       01 WS-CHOICE         PIC 9.
       01 WS-INDEX          PIC 9 VALUE 1.
       01 WS-COUNT          PIC 9 VALUE 0.
       01 RECORD-TABLE.
          05 RECORD-ENTRY OCCURS 5 TIMES.
             10 REC-ID      PIC 99 VALUE 0.
             10 REC-NAME    PIC X(20) VALUE SPACES.
             10 REC-AGE     PIC 99 VALUE 0.
       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM UNTIL WS-EOF = 'Y'
               DISPLAY "CRUD COBOL Application"
               DISPLAY "1 - Create"
               DISPLAY "2 - Read"
               DISPLAY "3 - Update"
               DISPLAY "4 - Delete"
               DISPLAY "5 - List"
               DISPLAY "9 - Exit"
               DISPLAY "Enter choice: " WITH NO ADVANCING
               ACCEPT WS-CHOICE
               EVALUATE WS-CHOICE
                   WHEN 1 PERFORM CREATE-REC
                   WHEN 2 PERFORM READ-REC
                   WHEN 3 PERFORM UPDATE-REC
                   WHEN 4 PERFORM DELETE-REC
                   WHEN 5 PERFORM LIST-RECS
                   WHEN 9 MOVE 'Y' TO WS-EOF
                   WHEN OTHER DISPLAY "Invalid choice"
               END-EVALUATE
           END-PERFORM
           DISPLAY "Goodbye."
           STOP RUN.
       CREATE-REC.
           IF WS-COUNT >= 5
               DISPLAY "Database full."
           ELSE
               ADD 1 TO WS-COUNT
               MOVE WS-COUNT TO WS-INDEX
               MOVE WS-COUNT TO REC-ID (WS-INDEX)
               DISPLAY "Enter name: " WITH NO ADVANCING
               ACCEPT REC-NAME (WS-INDEX)
               DISPLAY "Enter age: " WITH NO ADVANCING
               ACCEPT REC-AGE (WS-INDEX)
               DISPLAY "Created record " WS-INDEX
           END-IF.
       READ-REC.
           DISPLAY "Enter record id: " WITH NO ADVANCING
           ACCEPT WS-INDEX
           IF WS-INDEX >= 1 AND WS-INDEX <= WS-COUNT
              IF REC-ID (WS-INDEX) NOT = 0
                 DISPLAY "ID: " REC-ID (WS-INDEX)
                 DISPLAY "Name: " REC-NAME (WS-INDEX)
                 DISPLAY "Age: " REC-AGE (WS-INDEX)
              ELSE
                 DISPLAY "Record deleted or missing."
              END-IF
           ELSE
              DISPLAY "Invalid id."
           END-IF.
       UPDATE-REC.
           DISPLAY "Enter record id: " WITH NO ADVANCING
           ACCEPT WS-INDEX
           IF WS-INDEX >= 1 AND WS-INDEX <= WS-COUNT
              IF REC-ID (WS-INDEX) NOT = 0
                 DISPLAY "Enter new name: " WITH NO ADVANCING
                 ACCEPT REC-NAME (WS-INDEX)
                 DISPLAY "Enter new age: " WITH NO ADVANCING
                 ACCEPT REC-AGE (WS-INDEX)
                 DISPLAY "Updated."
              ELSE
                 DISPLAY "Record deleted."
              END-IF
           ELSE
              DISPLAY "Invalid id."
           END-IF.
       DELETE-REC.
           DISPLAY "Enter record id: " WITH NO ADVANCING
           ACCEPT WS-INDEX
           IF WS-INDEX >= 1 AND WS-INDEX <= WS-COUNT
              MOVE 0 TO REC-ID (WS-INDEX)
              MOVE SPACES TO REC-NAME (WS-INDEX)
              MOVE ZEROS TO REC-AGE (WS-INDEX)
              DISPLAY "Deleted record " WS-INDEX
           ELSE
              DISPLAY "Invalid id."
           END-IF.
       LIST-RECS.
           IF WS-COUNT = 0
               DISPLAY "No records."
           *> ELSE
               *> PERFORM VARYING WS-INDEX FROM 1 BY 1 UNTIL WS-INDEX > WS-COUNT
               *>    IF REC-ID (WS-INDEX) NOT = 0
               *>       DISPLAY "ID:" REC-ID (WS-INDEX) " Name:" REC-NAME (WS-INDEX) " Age:" REC-AGE (WS-INDEX)
               *>    END-IF
               *> END-PERFORM
           END-IF.
