unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    CheckBox1: TCheckBox;
    Edit1: TEdit;
    Memo1: TMemo;
    Memo2: TMemo;
    Memo3: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  i:integer;
  r:TRegExpr;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  r:=TRegExpr.Create(Edit1.Text);

  for i:=0 to Memo1.Lines.Count-1 do
  begin
     if r.Exec(Memo1.Lines.Strings[i]) then
     begin
          if CheckBox1.Checked=False then Memo3.Lines.Add(Memo2.Lines.Strings[i]);
     end
     else
     begin
         if CheckBox1.Checked=True then  Memo3.Lines.Add(Memo2.Lines.Strings[i]);
     end;
  end;
 // Sleep(300000);
end;

end.

