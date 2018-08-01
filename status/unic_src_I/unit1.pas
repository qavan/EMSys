unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  list:TStringList;

implementation

{$R *.lfm}
procedure RD(const stringList : TStringList) ;//RemoveDuplicates
var
  buffer: TStringList;
  cnt: Integer;
begin
  stringList.Sort;
  buffer := TStringList.Create;
  try
    buffer.Sorted := True;
    buffer.Duplicates := dupIgnore;
    buffer.BeginUpdate;
    for cnt := 0 to stringList.Count - 1 do
      buffer.Add(stringList[cnt]) ;
    buffer.EndUpdate;
    stringList.Assign(buffer) ;
  finally
    FreeandNil(buffer) ;
  end;
end;

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var x :integer;re:TRegExpr;t:string;
begin
  re:=TRegExpr.Create('.*:');
  list:=TStringList.Create;
  for x:=0 to Memo1.Lines.Count-1 do
    begin
      list.Append(Memo1.Lines.Strings[x]);
    end;
  RD(list);
  Memo1.Clear;
  memo1.Lines.AddStrings(list);
  for x:=0 to Memo1.Lines.Count-1 do
    begin
      if re.Exec(Memo1.Lines.Strings[x]) then
      begin
      t:=(re.Match[0]).replace(':','');
      memo2.Lines.Add('<f1>'+t+'<f2>'+t+'<f3>');
      end;
      end;
    end;


end.

